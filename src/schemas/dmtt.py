from typing import Optional

from pydantic import BaseModel, Field, constr

# from pydantic import BaseModel


class DmttBase(BaseModel):
    name: str
    person: str
    phone_number: str
    address: Optional[str] = None
    stir: str = None
    tg_user_id: Optional[str] = None
    is_active: bool = True

    class Config:
        from_attributes = True


class DmttInfo(BaseModel):
    name: str
    person: str
    phone_number: str
    address: str = None
    stir: str = None
    tg_user_id: str = None

    class Config:
        from_attributes = True


class DmttCreate(BaseModel):
    name: str
    person: str
    phone_number: str
    stir: str


class DmttUpdate(BaseModel):
    name: str
    person: str
    phone_number: str
    # stir: str
