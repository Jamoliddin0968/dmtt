# Your schemas for the app
from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    username: str
    password: str


class UserInfo(BaseModel):
    id: int
    name: str
    username: str

    class Config:
        from_attributes = True


class UserCreate(UserBase):
    pass
