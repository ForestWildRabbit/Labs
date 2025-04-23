from app.core.database import SessionLocal
from app.core.models import Item, User
from secrets import token_hex


def create_items():
    from app.core.data import items
    session = SessionLocal()
    items = [
        Item(**item) for item in items
    ]

    session.add_all(items)
    session.commit()


def create_users():
    from app.core.data import users
    session = SessionLocal()
    users = [
        User(**user, token=token_hex(16)) for user in users
    ]

    session.add_all(users)
    session.commit()
