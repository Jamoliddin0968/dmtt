# Your schemas for the app
from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    name: str
    username: str
    password: str


class UserInfo(BaseModel):
    id: int
    name: str
    username: str

    class ConfigDict:
        from_attributes = True


class UserCreate(UserBase):
    pass
