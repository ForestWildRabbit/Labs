import pytest
from starlette.testclient import TestClient
from ..data import items, users
from ..main import app
from ..database import engine
from ..prepare import create_items, create_users
from ..models import Base
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))


@pytest.fixture(scope="module")
def setup_database():
    # Drop and create tables
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # Create any initial items in the database
    create_items()
    create_users()


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
        "auth",
        json={"username": "test_user1' OR 1=1 -- ", "password": "doesn't_matter"}
    )
    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}


def test_auth_user(setup_database):
    client = TestClient(app)
    response = client.post(
        "auth",
        json={"username": "test_user1", "password": "hashed_test_password1"}
    )
    assert response.status_code == 200
    assert response.json() == users[0]

