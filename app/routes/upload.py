from fastapi import APIRouter, UploadFile
import os
import shutil

from app.utils.pdf_loader import load_pdf
from app.utils.chunking import chunk_text
from app.db.vector_store import create_vector_store

router = APIRouter()


@router.post("/upload")
async def upload_file(file: UploadFile):
    file_path = f"data/{file.filename}"
    os.makedirs("data", exist_ok=True)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = load_pdf(file_path)
    chunks = chunk_text(text)
    create_vector_store(chunks)

    return {"message": "File processed successfully"}



