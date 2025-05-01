
from sqlalchemy import update
from sqlalchemy.orm import Session
from app.core.models import User
from app.core.schemas import UpdateUser


def update_user_by_request(user_id: int, params: UpdateUser, session: Session):
    statement = (update(User)
                 .where(User.id == user_id)
                 .values(**params.model_dump(exclude_none=True))
                 )
    session.execute(statement)
    session.commit()


def get_user_by_id(user_id: int, session: Session) -> User | None:
    result = (session.query(User)
              .filter(User.id == user_id).first())

    return result
