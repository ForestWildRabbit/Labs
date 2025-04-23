from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    description: str
    released: bool


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int


class UserBase(BaseModel):
    username: str
    password: str


class UserLogin(UserBase):
    pass


class UserAuth(BaseModel):
    token: str


class User(UserBase):
    id: int


class ReadUser(BaseModel):
    username: str


class UpdateUser(BaseModel):
    username: str | None = None
