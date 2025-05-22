from pydantic import BaseModel, Field


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


class UserAuthMFA(BaseModel):
    username: str = Field(min_length=4, max_length=20)
    password: str
    totp_token: str


class User(UserBase):
    id: int


class ReadUser(BaseModel):
    username: str


class UpdateUser(BaseModel):
    username: str | None = None
