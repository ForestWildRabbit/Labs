from database import SessionLocal
from models import Item, User


def create_items():
    from data import items
    session = SessionLocal()
    items = [
        Item(**item) for item in items
    ]

    session.add_all(items)
    session.commit()


def create_users():
    from data import users
    session = SessionLocal()
    users = [
        User(**user) for user in users
    ]

    session.add_all(users)
    session.commit()
