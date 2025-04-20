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


class UserAuth(UserBase):
    pass


class User(UserBase):
    id: int

