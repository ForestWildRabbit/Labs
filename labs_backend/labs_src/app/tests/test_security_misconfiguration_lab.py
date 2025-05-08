import base64

from starlette.testclient import TestClient

from app.core.data import ADMIN_USERNAME, ADMIN_PASSWORD
from app.core.main import app


def get_basic_auth_header(username: str, password: str):
    credentials = f"{username}:{password}"
    encoded = base64.b64encode(credentials.encode()).decode()
    return {"Authorization": f"Basic {encoded}"}


def test_docs_unauthorized(setup_database):
    client = TestClient(app)
    response = client.get("docs")

    assert response.status_code == 401


def test_openapi_unauthorized(setup_database):
    client = TestClient(app)
    response = client.get("openapi.json")

    assert response.status_code == 401


def test_docs_with_wrong_credentials(setup_database):
    client = TestClient(app)
    headers = get_basic_auth_header("wrong_username", "wrong_password")
    response = client.get("docs", headers=headers)

    assert response.status_code == 401
    assert response.json() == {"detail": "Unauthorized"}


def test_openapi_with_wrong_credentials(setup_database):
    client = TestClient(app)
    headers = get_basic_auth_header("wrong_username", "wrong_password")
    response = client.get("openapi.json", headers=headers)

    assert response.status_code == 401
    assert response.json() == {"detail": "Unauthorized"}


def test_docs_authorized(setup_database):
    client = TestClient(app)
    headers = get_basic_auth_header(ADMIN_USERNAME, ADMIN_PASSWORD)
    response = client.get("docs", headers=headers)

    assert response.status_code == 200


def test_openapi_authorized(setup_database):
    client = TestClient(app)
    headers = get_basic_auth_header(ADMIN_USERNAME, ADMIN_PASSWORD)
    response = client.get("openapi.json", headers=headers)

    assert response.status_code == 200
