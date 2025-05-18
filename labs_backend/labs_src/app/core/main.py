from fastapi import FastAPI, Depends
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

from app.core.routers import items_router, users_router, jwt_router, file_router
from app.student_code.code_security_misconfiguration_lab import verify_admin_credentials

app = FastAPI(docs_url=None, openapi_url=None)

app.include_router(items_router)
app.include_router(users_router)
app.include_router(jwt_router)
app.include_router(file_router)


@app.get("/docs", include_in_schema=False)
def custom_docs(_=Depends(verify_admin_credentials)):
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Docs")


@app.get("/openapi.json", include_in_schema=False)
def openapi(_=Depends(verify_admin_credentials)):
    return get_openapi(title="Lab API", version="1.0", routes=app.routes)
