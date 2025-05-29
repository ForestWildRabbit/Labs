import pytest
from starlette.testclient import TestClient
from app.core.main import app

client = TestClient(app)

solution_dir = "./labs_src/app/solutions"


def test_upload_no_files():
    response = client.post("/upload", )
    assert response.status_code == 422
    assert 'detail' in response.json()


def test_upload_with_wrong_lab_name():
    file_path = "./labs_src/requirements.txt"

    with open(file_path, "rb") as f:
        files = {
            "file": ("testfile.txt", f, "text/plain")
        }
        data = {
            "lab_name": "wrong_lab_name"
        }
        response = client.post("/upload", files=files, data=data)

    assert response.status_code == 422
    assert 'detail' in response.json()


@pytest.mark.parametrize("file_path,lab_name",
                         [
                             (f"{solution_dir}/solution_sql_injection_lab.py",
                              "sql_injection_lab"),
                             (f"{solution_dir}/solution_broken_access_control_lab.py",
                              "broken_access_control_lab"),
                             (f"{solution_dir}/solution_cryptographic_failures_lab.py",
                              "cryptographic_failures_lab"),
                             (f"{solution_dir}/solution_security_misconfiguration_lab.py",
                              "security_misconfiguration_lab"),
                             (f"{solution_dir}/solution_insecure_design_lab.py",
                              "insecure_design_lab"),
                             (f"{solution_dir}/solution_security_logging_failures_lab.py",
                              "security_logging_failures_lab"),
                         ])
def test_upload_file(file_path, lab_name):
    with open(file_path, "rb") as f:
        files = {
            "file": ("testfile.txt", f, "text/plain")
        }
        data = {
            "lab_name": lab_name
        }
        response = client.post("/upload", files=files, data=data)

    assert response.status_code == 200
