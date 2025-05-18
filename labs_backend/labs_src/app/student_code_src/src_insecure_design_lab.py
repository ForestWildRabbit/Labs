from fastapi import HTTPException, UploadFile, File
import os

# tested by /app/tests/test_insecure_design_lab.py

'''
Secure the upload file endpoint by validating file types
(only ".png" and ".jpeg" file extensions are valid)
and save it from directory traversal attacks.
Filename may contain a path e.g. "../../secret_directory/example.png"
You should save it as "example.png" in ./app/static/uploaded directory.
'''

async def upload_image_handler(file: UploadFile = File(...)):

    contents = await file.read()
    with open(f"./app/static/uploaded/{file.filename}", "wb") as f:
        f.write(contents)
    return {"filename": file.filename}
