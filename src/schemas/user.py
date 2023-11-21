# Your schemas for the app
from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    username: str
    password: str


class UserInfo(UserBase):
    pass


class UserCreate(UserBase):
    pass
