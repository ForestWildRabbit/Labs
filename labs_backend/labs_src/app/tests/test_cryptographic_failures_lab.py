
from starlette.testclient import TestClient
from app.core.main import app

"""
There are some tests for cryptographic_failures_lab.
Some tests will try to authorize with a generated token or without any credentials.
Your task is to make the given jwt authorization to work correctly.
"""

def test_jwt_auth_unauthorized_header_missing(setup_database):
    client = TestClient(app)
    response = client.get("jwt/auth")

    assert response.status_code == 401
    assert response.json() == {'detail': 'Authorization header missing'}


def test_jwt_auth_unauthorized_invalid_token_format(setup_database):
    client = TestClient(app)
    response = client.get("jwt/auth", headers={'Authorization': 'invalid_token_format'})

    assert response.status_code == 401
    assert response.json() == {'detail': 'Invalid token format'}


def test_jwt_auth_unauthorized_invalid_token(setup_database):
    client = TestClient(app)
    response = client.get("jwt/auth", headers={'Authorization': 'Bearer abcdef'})

    assert response.status_code == 401
    assert response.json() == {'detail': 'Invalid token'}


def test_jwt_auth_unauthorized_forged_token(setup_database):
    import jwt
    client = TestClient(app)
    user_id = 5
    forged_token = jwt.encode({"username": f"test_user{user_id}"}, key=None, algorithm="none")

    response = client.get("jwt/auth",
                          headers={'Authorization': f'Bearer {forged_token}'})

    assert response.status_code == 401, "Accepts forged tokens"
    assert response.json() == {'detail': 'Invalid token'}


def test_jwt_auth(setup_database):
    client = TestClient(app)
    user_id = 5
    response = client.post("jwt/login",
                           json={"username": f"test_user{user_id}",
                                 "password": f"hashed_test_password{user_id}"
                                 })

    assert response.status_code == 200

    token = response.json().get("token")

    response = client.get("jwt/auth",
                          headers={'Authorization': f'Bearer {token}'})

    assert response.status_code == 200
    assert response.json() == {'username': f"test_user{user_id}"}

