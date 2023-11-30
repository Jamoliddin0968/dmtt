from uuid import UUID

from pydantic import BaseModel


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str


class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None


class UserOut(BaseModel):
    id: UUID
    email: str


class SystemUser(UserOut):
    password: str
