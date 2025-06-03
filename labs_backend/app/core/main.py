from pathlib import Path

from fastapi import FastAPI, UploadFile, File, HTTPException, Response, Form
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from enum import Enum
import shutil
from fastapi.responses import FileResponse


class LabName(str, Enum):
    sql_injection_lab = "sql_injection_lab"
    broken_access_control_lab = "broken_access_control_lab"
    cryptographic_failures_lab = "cryptographic_failures_lab"
    security_misconfiguration_lab = "security_misconfiguration_lab"
    insecure_design_lab = "insecure_design_lab"
    security_logging_failures_lab = "security_logging_failures_lab"
    C01_vulnerable_dependencies_lab = "C01_vulnerable_dependencies_lab"
    C02_access_control_lab = "C02_access_control_lab"
    C03_file_handling_lab = "C03_file_handling_lab",
    C04_insufficient_authentication_lab = "C04_insufficient_authentication_lab",
    C05_code_injection_lab = "C05_code_injection_lab",
    C06_command_injection_lab = "C06_command_injection_lab",
    C07_weak_cryptography_lab = "C07_weak_cryptography_lab",
    C08_privilege_escalation_lab = "C08_privilege_escalation_lab",
    C09_authentication_bypass_lab = "C09_authentication_bypass_lab",
    C10_race_conditions_lab = "C10_race_conditions_lab",


class NoCacheStaticFiles(StaticFiles):
    async def get_response(self, path, scope):
        response: Response = await super().get_response(path, scope)
        response.headers["Cache-Control"] = "no-store"
        return response


app = FastAPI()

app.mount("/static", NoCacheStaticFiles(directory="labs_src"), name="labs")

UPLOAD_DIR = Path("labs_src/app/student_code")
SRC_DIR = Path("labs_src/app/student_code_src")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/upload")
async def upload_file(file: UploadFile = File(...),
                      lab_name: LabName = Form(...)) -> FileResponse:

    filename = f'code_{lab_name.value}.py'
    file_path = UPLOAD_DIR / filename

    try:
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save file: {e}")

    zip_path = Path("labs_src.zip")
    shutil.make_archive("labs_src", "zip", "labs_src")

    src_path = SRC_DIR / f'src_{lab_name.value}.py'
    dst_path = UPLOAD_DIR / f'code_{lab_name.value}.py'
    shutil.copyfile(src_path, dst_path)

    return FileResponse(zip_path, filename="labs_src.zip", media_type="application/zip")
