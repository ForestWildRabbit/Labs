
from starlette.testclient import TestClient

from app.core.main import app

import filecmp

STATIC_PATH = '/labs_src/app/static'


def test_png_image_file_upload(setup_database):
    client = TestClient(app)
    image_file_name = 'image'
    with open(f"{STATIC_PATH}/images/{image_file_name}.png", "rb") as f:
        response = client.post(
            "file/upload",
            files={"file": (f"{image_file_name}_uploaded.png", f, "image/png")}
        )

    assert response.status_code == 200
    assert response.json() == {"filename": f"{image_file_name}_uploaded.png"}


def test_jpeg_image_file_upload(setup_database):
    client = TestClient(app)
    image_file_name = 'image'
    with open(f"{STATIC_PATH}/images/{image_file_name}.jpeg", "rb") as f:
        response = client.post(
            "file/upload",
            files={"file": (f"{image_file_name}_uploaded.jpeg", f, "image/jpeg")}
        )

    assert response.status_code == 200
    assert response.json() == {"filename": f"{image_file_name}_uploaded.jpeg"}


def test_text_file_upload(setup_database):
    client = TestClient(app)
    text_file_name = 'text'
    with open(f"{STATIC_PATH}/texts/{text_file_name}.txt", "rb") as f:
        response = client.post(
            "file/upload",
            files={"file": (f"{text_file_name}_uploaded.txt", f, "text/txt")}
        )

    assert response.status_code == 400
    assert response.json() == {'detail': 'Invalid file type'}


def test_script_file_upload(setup_database):
    client = TestClient(app)
    script_file_name = 'script'
    with open(f"{STATIC_PATH}/scripts/{script_file_name}.sh", "rb") as f:
        response = client.post(
            "file/upload",
            files={"file": (f"{script_file_name}_uploaded.sh", f)}
        )

    assert response.status_code == 400
    assert response.json() == {'detail': 'Invalid file type'}


def test_traversal_image_file_upload(setup_database):
    client = TestClient(app)
    image_file_path = f"{STATIC_PATH}/images/image.png"
    secret_filename = 'secret'
    secret_file_path = f"{STATIC_PATH}/secrets/{secret_filename}.png"
    secret_file_path_copy = f"{STATIC_PATH}/secrets/{secret_filename}_copy.png"
    uploaded_image_file_path = f"{STATIC_PATH}/uploaded/secret.png"

    with open(image_file_path, "rb") as f:
        response = client.post(
            "file/upload",
            files={"file": (f"../secrets/{secret_filename}.png", f, "image/png")}
        )

    assert filecmp.cmp(secret_file_path_copy, secret_file_path, shallow=False) is True, \
        'The secret file has been replaced by a directory traversal attack'
    assert filecmp.cmp(image_file_path, uploaded_image_file_path, shallow=False) is True, \
        'The uploaded file must be in /app/static/uploaded directory'
    assert response.status_code == 200
    assert response.json() == {"filename": f"{secret_filename}.png"}
