import torch
import torch.nn as nn
import numpy as np
import porespy as ps
import numpy as np
import pygltflib
import numpy as np
from stl import mesh
from math import sqrt

def normalize(vector):
    norm = 0
    for i in range(0, len(vector)):
        norm += vector[i] * vector [i]
    norm = sqrt(norm)
    for i in range(0, len(vector)):
        vector[i] = vector[i] / norm

    return vector


def stl_to_glb(file):
    stl_mesh = mesh.Mesh.from_file(file)

    stl_points = []
    for i in range(0, len(stl_mesh.points)): # Convert points into correct numpy array
        stl_points.append([stl_mesh.points[i][0],stl_mesh.points[i][1],stl_mesh.points[i][2]])
        stl_points.append([stl_mesh.points[i][3],stl_mesh.points[i][4],stl_mesh.points[i][5]])
        stl_points.append([stl_mesh.points[i][6],stl_mesh.points[i][7],stl_mesh.points[i][8]])

    points = np.array(
        stl_points,
        dtype="float32",
    )

    stl_normals = []
    for i in range(0, len(stl_mesh.normals)): # Convert points into correct numpy array
        normal_vector = [stl_mesh.normals[i][0],stl_mesh.normals[i][1],stl_mesh.normals[i][2]]
        normal_vector = normalize(normal_vector)
        stl_normals.append(normal_vector)
        stl_normals.append(normal_vector)
        stl_normals.append(normal_vector)

    normals = np.array(
        stl_normals,
        dtype="float32"
    )

    points_binary_blob = points.tobytes()
    normals_binary_blob = normals.tobytes()

    gltf = pygltflib.GLTF2(
        scene=0,
        scenes=[pygltflib.Scene(nodes=[0])],
        nodes=[pygltflib.Node(mesh=0)],
        meshes=[
            pygltflib.Mesh(
                primitives=[
                    pygltflib.Primitive(
                        attributes=pygltflib.Attributes(POSITION=0, NORMAL=1), indices=None
                    )
                ]
            )
        ],
        accessors=[
            pygltflib.Accessor(
                bufferView=0,
                componentType=pygltflib.FLOAT,
                count=len(points),
                type=pygltflib.VEC3,
                max=points.max(axis=0).tolist(),
                min=points.min(axis=0).tolist(),
            ),
            pygltflib.Accessor(
                bufferView=1,
                componentType=pygltflib.FLOAT,
                count=len(normals),
                type=pygltflib.VEC3,
                max=None,
                min=None,
            ),
        ],
        bufferViews=[
            pygltflib.BufferView(
                buffer=0,
                byteOffset=0,
                byteLength=len(points_binary_blob),
                target=pygltflib.ARRAY_BUFFER,
            ),
            pygltflib.BufferView(
                buffer=0,
                byteOffset=len(points_binary_blob),
                byteLength=len(normals_binary_blob),
                target=pygltflib.ARRAY_BUFFER,
            ),
        ],
        buffers=[
            pygltflib.Buffer(
                byteLength=len(points_binary_blob) + len(normals_binary_blob)
            )
        ],
    )
    gltf.set_binary_blob(points_binary_blob + normals_binary_blob)
    gltf.save("porous/output.glb")



device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
class ConvLSTMCell(nn.Module):

    def __init__(self, in_channels, out_channels,
    kernel_size, padding, activation, frame_size):

        super(ConvLSTMCell, self).__init__()

        if activation == "tanh":
            self.activation = torch.tanh
        elif activation == "relu":
            self.activation = torch.relu

        # Idea adapted from https://github.com/ndrplz/ConvLSTM_pytorch
        self.conv = nn.Conv2d(
            in_channels=in_channels + out_channels,
            out_channels=4 * out_channels,
            kernel_size=kernel_size,
            padding=padding)

        # Initialize weights for Hadamard Products
        self.W_ci = nn.Parameter(torch.Tensor(out_channels, *frame_size))
        self.W_co = nn.Parameter(torch.Tensor(out_channels, *frame_size))
        self.W_cf = nn.Parameter(torch.Tensor(out_channels, *frame_size))

    def forward(self, X, H_prev, C_prev):

        # Idea adapted from https://github.com/ndrplz/ConvLSTM_pytorch
        conv_output = self.conv(torch.cat([X, H_prev], dim=1))

        # Idea adapted from https://github.com/ndrplz/ConvLSTM_pytorch
        i_conv, f_conv, C_conv, o_conv = torch.chunk(conv_output, chunks=4, dim=1)

        input_gate = torch.sigmoid(i_conv + self.W_ci * C_prev )
        forget_gate = torch.sigmoid(f_conv + self.W_cf * C_prev )

        # Current Cell output
        C = forget_gate*C_prev + input_gate * self.activation(C_conv)

        output_gate = torch.sigmoid(o_conv + self.W_co * C )

        # Current Hidden State
        H = output_gate * self.activation(C)

        return H, C

class ConvLSTM(nn.Module):

    def __init__(self, in_channels, out_channels,
    kernel_size, padding, activation, frame_size):

        super(ConvLSTM, self).__init__()

        self.out_channels = out_channels

        # We will unroll this over time steps
        self.convLSTMcell = ConvLSTMCell(in_channels, out_channels,
        kernel_size, padding, activation, frame_size)

    def forward(self, X):

        # X is a frame sequence (batch_size, num_channels, seq_len, height, width)

        # Get the dimensions
        batch_size, _, seq_len, height, width = X.size()

        # Initialize output
        output = torch.zeros(batch_size, self.out_channels, seq_len,
        height, width, device=device)

        # Initialize Hidden State
        H = torch.zeros(batch_size, self.out_channels,
        height, width, device=device)

        # Initialize Cell Input
        C = torch.zeros(batch_size,self.out_channels,
        height, width, device=device)

        # Unroll over time steps
        for time_step in range(seq_len):

            H, C = self.convLSTMcell(X[:,:,time_step], H, C)

            output[:,:,time_step] = H

        return output

class Seq2Seq(nn.Module):

    def __init__(self, num_channels, num_kernels, kernel_size, padding,
    activation, frame_size, num_layers):

        super(Seq2Seq, self).__init__()

        self.sequential = nn.Sequential()

        # Add First layer (Different in_channels than the rest)
        self.sequential.add_module(
            "convlstm1", ConvLSTM(
                in_channels=num_channels, out_channels=num_kernels,
                kernel_size=kernel_size, padding=padding,
                activation=activation, frame_size=frame_size)
        )

        self.sequential.add_module(
            "batchnorm1", nn.BatchNorm3d(num_features=num_kernels)
        )

        # Add rest of the layers
        for l in range(2, num_layers+1):

            self.sequential.add_module(
                f"convlstm{l}", ConvLSTM(
                    in_channels=num_kernels, out_channels=num_kernels,
                    kernel_size=kernel_size, padding=padding,
                    activation=activation, frame_size=frame_size)
                )

            self.sequential.add_module(
                f"batchnorm{l}", nn.BatchNorm3d(num_features=num_kernels)
                )

        # Add Convolutional Layer to predict output frame
        self.conv = nn.Conv2d(
            in_channels=num_kernels, out_channels=num_channels,
            kernel_size=kernel_size, padding=padding)

    def forward(self, X):

        # Forward propagation through all the layers
        output = self.sequential(X)

        # Return only the last output frame
        output = self.conv(output[:,:,-1])

        return nn.Sigmoid()(output)

model = Seq2Seq(num_channels=1, num_kernels=64,
kernel_size=(3, 3), padding=(1, 1), activation="relu",
frame_size=(64,64), num_layers=1).to(device)
model_state_dict = torch.load('model/model_20.pth',map_location=torch.device('cpu'))
model.load_state_dict(model_state_dict)

def prediction_porous(image):
    print("prediction_porous")
    image=image.reshape((1, 10,64,64))
    image = torch.tensor(image).unsqueeze(1)
    image = image.to(device)
    output = np.zeros((1,10,64,64), dtype=np.uint8)
# Loop over timesteps
    for timestep in range(10):
        input = image[:,:,timestep:timestep+1]
        output[:,timestep]=(model(input).squeeze(1).cpu()>0.5)
    ps.io.to_stl(output[0],"output.stl")
    print("done")
    stl_to_glb("output.stl")
    return  {"url":"model/output/output.glb"}
