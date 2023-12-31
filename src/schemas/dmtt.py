from typing import Optional

from pydantic import BaseModel


class DmttInfo(BaseModel):
    id: int
    name: str
    person: str
    phone_number: str
    address: Optional[str] = None
    stir: Optional[str] = None
    tg_user_id: Optional[str] = None

    class ConfigDict:
        from_attributes = True


class DmttCreate(BaseModel):
    name: str
    person: str
    phone_number: str
    stir: str


class DmttUpdate(DmttCreate):
    pass
