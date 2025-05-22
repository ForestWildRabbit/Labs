from sqlalchemy import update
from sqlalchemy.orm import Session
from app.core.models import User
from app.core.schemas import UpdateUser
from random import randint
import csv

STATIC_PATH = '/labs_src/app/static'


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


def scan_most_common_passwords():
    with open(f"{STATIC_PATH}/tables/common_passwords.csv", "r") as f:
        most_common_passwords = []
        reader = csv.reader(f, delimiter=",")
        for line in reader:
            most_common_passwords.append(line[0])

        return most_common_passwords


def generate_totp(length=4) -> str:
    n = randint(1, 10 ** length - 1)
    str_n = str(n)
    return f"{'0' * (length - len(str_n))}{str_n}"

