import pytest

from starlette.testclient import TestClient
from app.core.data import most_common_passwords
from app.core.main import app


def find_correct_password(client: TestClient, username: str) -> str:
    for password in most_common_passwords:
        response = client.post("mfa/login",
                               json={'username': username, 'password': password, 'totp_token': '1234'})
        if response.json() != {'detail': 'Wrong password'}:
            return password


def find_correct_totp(client: TestClient, username: str, password: str, length=4) -> str:
    for i in range(10 ** length):
        totp = f"{'0' * (length - len(str(i)))}{i}"
        response = client.post("mfa/login",
                               json={'username': username, 'password': password, 'totp_token': totp})
        if response.status_code == 200:
            return totp
    return '0' * length


def full_enumeration(client: TestClient, username: str, length=4) -> bool:
    for password in most_common_passwords:
        for i in range(10 ** length):
            totp = f"{'0' * (length - len(str(i)))}{i}"
            response = client.post("mfa/login",
                                   json={'username': username, 'password': password, 'totp_token': totp})
            if response.status_code == 429:
                return False
            if response.status_code == 200:
                return True
    return True


def test_mfa_auth_with_wrong_credentials(setup_database):
    client = TestClient(app)
    response = client.post("mfa/login", json={'username': 'wrong', 'password': '111111', 'totp_token': '1111'})

    assert response.status_code == 400
    assert response.json() == {'detail': 'Wrong credentials'}


@pytest.mark.timeout(60)
def test_mfa_auth_with_single_enumeration(setup_database):
    client = TestClient(app)
    test_username = "test_mfa_user"
    test_password = find_correct_password(client, test_username)
    test_totp = find_correct_totp(client, test_username, test_password)

    response = client.post("mfa/login",
                           json={'username': test_username, 'password': test_password, 'totp_token': test_totp})

    assert response.status_code == 400


def test_mfa_auth_with_full_enumeration(setup_database):
    client = TestClient(app)
    test_username = "test_mfa_user"
    assert full_enumeration(client, test_username) is False
