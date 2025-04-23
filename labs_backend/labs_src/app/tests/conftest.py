import pytest

from app.core.database import engine
from app.core.prepare import create_items, create_users
from app.core.models import Base


@pytest.fixture(scope="session")
def setup_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    create_items()
    create_users()
