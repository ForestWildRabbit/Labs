from fastapi import HTTPException, UploadFile, File
import os

ALLOWED_CONTENT_TYPES = {"image/jpeg", "image/png"}


async def upload_image_handler(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(status_code=400, detail="Invalid file type")

    filename = os.path.basename(file.filename)
    upload_directory = './app/static/uploaded/'
    save_path = os.path.join(upload_directory, filename)
    contents = await file.read()
    with open(save_path, "wb") as f:
        f.write(contents)
    return {"filename": filename}