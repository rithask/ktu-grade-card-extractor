from fastapi import FastAPI, File, UploadFile, HTTPException
from utils import handle_pdf
import tempfile
import os
import logging

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "beep boop"}

@app.post("/")
async def upload_file(file: UploadFile = File(...)):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name
        data = handle_pdf(tmp_path)

        return data
    
    except Exception as e:
        logging.error(f"Error processing file: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
