from typing import Optional, List

from pydantic import BaseModel


class PersonInfo(BaseModel):
    first_name: str = None
    last_name: str = None
    phone_number: str = None
    tg_user_id: str = None


class DmttInfo(BaseModel):
    id: int
    name: str
    phone_number: str
    address: Optional[str] = None
    stir: Optional[str] = None

    persons: List[PersonInfo]

    class ConfigDict:
        from_attributes = True


class DmttCreate(BaseModel):
    name: str
    phone_number: str
    stir: Optional[str]


class DmttUpdate(DmttCreate):
    pass


class PersonCreate(BaseModel):
    dmtt_id: int
    first_name: str
    last_name: str
    phone_number: str
    rank: int
    tg_user_id: str = None


class PersonUpdate(BaseModel):
    first_name: str = None
    last_name: str = None
    phone_number: str = None
    tg_user_id: str = None
