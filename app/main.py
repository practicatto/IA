from fastapi import File, UploadFile, FastAPI, File,HTTPException, responses
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
import numpy as np
from model.model import prediction_porous
from starlette.responses import FileResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)
file_path = ""

@app.get("/")
def index():
    return {"Welcome prediction porous medium"}

@app.get('/models/output', response_class=responses.FileResponse)
async def view():
    path = os.path.join(file_path, f"output/output.glb")
    print("path : ",path)
    if os.path.exists(path):
       print("path : ",path)
       return responses.FileResponse(path)
    else:
        raise HTTPException(status_code=404, detail="File not found")

@app.get('download/output')
async def download():
    path = os.path.join(file_path, f"output/output.glb")
    if os.path.exists(path):
        FileResponse(file_path, media_type='application/octet-stream',filename="output.glb")
    else:
        raise HTTPException(status_code=404, detail="File not found")


@app.post("/prediction")
def prediction(file: UploadFile = File(...)):
    try:
        with open(file.filename, 'wb') as f:
            shutil.copyfileobj(file.file, f)
            image = np.load(file.filename).astype(np.int)
            res = prediction_porous(image)
            return res
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
