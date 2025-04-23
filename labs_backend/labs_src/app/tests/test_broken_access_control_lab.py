from starlette.testclient import TestClient
from app.core.main import app


def test_update_users_unauthorized_header_missing(setup_database):
    client = TestClient(app)
    response = client.patch("users/5", json={'username': 'updated_test_user'})

    assert response.status_code == 401
    assert response.json() == {'detail': 'Authorization header missing'}


def test_update_users_unauthorized_invalid_token_format(setup_database):
    client = TestClient(app)
    response = client.patch("users/5",
                            json={'username': 'updated_test_user'},
                            headers={'Authorization': 'invalid_token_format'})

    assert response.status_code == 401
    assert response.json() == {'detail': 'Invalid token format'}


def test_update_users_unauthorized_invalid_token(setup_database):
    client = TestClient(app)
    response = client.patch("users/5",
                            json={'username': 'updated_test_user'},
                            headers={'Authorization': 'Bearer abcdef'})

    assert response.status_code == 401
    assert response.json() == {'detail': 'Invalid token'}


def test_update_users_forbidden(setup_database):
    client = TestClient(app)
    response = client.post(
        "users/auth",
        json={"username": "test_user5", "password": "hashed_test_password5"}
    )
    token = response.json().get('token', '')
    response = client.patch("users/4",
                            json={'username': 'updated_test_user'},
                            headers={'Authorization': f'Bearer {token}'})

    assert response.status_code == 403
    assert response.json() == {'detail': 'Not authorized to perform this action'}


def test_update_users(setup_database):
    client = TestClient(app)
    response = client.post(
        "users/auth",
        json={"username": "test_user5", "password": "hashed_test_password5"}
    )
    token = response.json().get('token', '')

    user_id = 5
    updated_username = f'updated_test_user{user_id}'

    client.patch(f"users/{user_id}",
                 json={'username': updated_username},
                 headers={'Authorization': f'Bearer {token}'})

    response = client.get(f"users/{user_id}")
    assert response.json() == {'username': updated_username}

