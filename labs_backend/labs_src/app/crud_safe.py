from sqlalchemy import text, select
from sqlalchemy.orm import Session
from models import Item, User
from schemas import UserAuth


# Get released item by name
def get_item_by_name(session: Session, name: str) -> Item | None:
    raw_sql = text("SELECT * FROM items WHERE name = :name AND released = TRUE")
    result = session.execute(raw_sql, {'name': name})
    return result.fetchone()


def delete_item_by_name(session: Session, name: str) -> bool:
    item = session.query(Item).filter(Item.name == name).first()

    if item:
        session.delete(item)
        session.commit()
        return True
    else:
        return False


# Check user's credentials
def user_auth(session: Session, user: UserAuth) -> User | None:
    result = (session.query(User)
              .filter(User.username == user.username, User.password == user.password).first())
    return result