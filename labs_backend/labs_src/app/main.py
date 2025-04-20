
from fastapi import FastAPI, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from database import get_db
from crud import get_item_by_name, user_auth, delete_item_by_name
from schemas import Item, UserAuth, User

app = FastAPI()


@app.get("/items/{name}", response_model=Item)
def get_item(name: str, session: Session = Depends(get_db)):
    item = get_item_by_name(session, name)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.delete("/items/{name}")
def delete_item(name: str, session: Session = Depends(get_db)):
    item = delete_item_by_name(session, name)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return Response(status_code=204)


@app.post("/auth", response_model=User)
def authenticate(user: UserAuth, session: Session = Depends(get_db)):
    user = user_auth(session, user)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# @app.get("/items/{item_id}", response_model=Item)
# def read_item(item_id: int, db: Session = Depends(get_db)):
#     db_item = get_item(db, item_id=item_id)
#     if db_item is None:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return db_item


