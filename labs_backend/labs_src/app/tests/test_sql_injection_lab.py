
from starlette.testclient import TestClient

from app.core.data import items
from app.core.main import app

"""
There are some tests for sql_injection_lab.
Some tests will try to simulate sql injection attacks.
Your task is to make the application safe to sql injections.
"""


def test_get_items_injection(setup_database):
    client = TestClient(app)
    response = client.get("items/item4' OR 1=1 -- ")

    assert response.status_code == 404
    assert response.json() == {'detail': 'Item not found'}


def test_get_items(setup_database):
    client = TestClient(app)
    response = client.get("items/item5")

    assert response.status_code == 200
    assert response.json() == items[4]


def test_delete_item_injection(setup_database):
    client = TestClient(app)
    response = client.delete("items/item5' OR 1=1 -- ")

    assert response.status_code == 404
    assert response.json() == {'detail': 'Item not found'}


# will not pass if injected
def test_delete_item(setup_database):
    client = TestClient(app)
    response = client.delete("items/item1")

    assert response.status_code == 204


def test_auth_user_injection(setup_database):
    client = TestClient(app)
    response = client.post(
        "users/auth",
        json={"username": "test_user1' OR 1=1 -- ", "password": "doesn't_matter"}
    )
    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}


def test_auth_user(setup_database):
    client = TestClient(app)
    response = client.post(
        "users/auth",
        json={"username": "test_user1", "password": "hashed_test_password1"}
    )
    assert response.status_code == 200

