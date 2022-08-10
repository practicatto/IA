from fastapi import File, UploadFile, FastAPI
import shutil
import numpy as np

app = FastAPI()


@app.get("/")
def index():
    return {"Welcome prediction porous medium"}


@app.post("/prediction")
def prediction(file: UploadFile = File(...)):
    try:
        with open(file.filename, 'wb') as f:
            shutil.copyfileobj(file.file, f)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
    return {"message": f"Successfully uploaded {file.filename}"}
