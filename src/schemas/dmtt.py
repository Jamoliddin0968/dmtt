from typing import Optional

from pydantic import BaseModel


class DmttBase(BaseModel):
    name: str
    person: str
    phone_number: str
    address: Optional[str] = None
    stir: Optional[str] = None
    tg_user_id: Optional[str] = None
    is_active: bool = True

    class Config:
        from_attributes = True


class DmttInfo(BaseModel):
    name: str
    person: str
    phone_number: str
    address: Optional[str] = None
    stir: Optional[str] = None
    tg_user_id: Optional[str] = None

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
    # stir: str  # Uncomment this line if needed for the update
