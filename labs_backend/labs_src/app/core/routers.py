from fastapi import Depends, HTTPException, Response
from sqlalchemy.orm import Session

from app.core.utils import update_user_by_request, get_user_by_id
from app.student_code.code_broken_access_control_lab import is_owner
from app.student_code.code_sql_injection_lab import get_item_by_name, user_auth, delete_item_by_name

from app.core.database import get_db
from app.core.schemas import Item, UserLogin, UpdateUser, UserAuth, ReadUser
from fastapi import APIRouter

items_router = APIRouter(
    prefix='/items',
    tags=['Items'],
)


@items_router.get("/{name}", response_model=Item)
def get_item(name: str, session: Session = Depends(get_db)):
    item = get_item_by_name(session, name)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@items_router.delete("/{name}")
def delete_item(name: str, session: Session = Depends(get_db)):
    item = delete_item_by_name(session, name)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return Response(status_code=204)


users_router = APIRouter(
    prefix='/users',
    tags=['Users'],
)


@users_router.post("/auth", response_model=UserAuth)
def authenticate(user: UserLogin, session: Session = Depends(get_db)):
    user = user_auth(session, user)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@users_router.get("/{user_id}", response_model=ReadUser)
def get_user(user_id, session: Session = Depends(get_db)):
    user = get_user_by_id(user_id, session)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@users_router.patch("/{user_id}")
def update_user(user_id, params: UpdateUser,
                _permission=Depends(is_owner),
                session: Session = Depends(get_db)):
    update_user_by_request(user_id, params, session)
    return Response(status_code=204)



