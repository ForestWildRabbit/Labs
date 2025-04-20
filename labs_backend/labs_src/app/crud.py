from sqlalchemy import text
from sqlalchemy.orm import Session
from models import Item, User
from schemas import UserAuth


# Get released item by name
def get_item_by_name(session: Session, name: str) -> Item | None:
    raw_sql = text(f"SELECT * FROM items WHERE name = '{name}' AND released = TRUE")
    result = session.execute(raw_sql)
    return result.fetchone()


def delete_item_by_name(session: Session, name: str) -> bool:
    raw_sql = text(f"DELETE FROM items WHERE name = '{name}'")
    result = session.execute(raw_sql)
    return result.rowcount > 0


# Check user's credentials
def user_auth(session: Session, user: UserAuth) -> User | None:
    raw_sql = text(f"SELECT * FROM users WHERE username = '{user.username}' AND password = '{user.password}'")
    result = session.execute(raw_sql)
    return result.fetchone()
