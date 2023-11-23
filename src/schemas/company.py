from pydantic import BaseModel, ConfigDict, EmailStr


class CompanyInfo(BaseModel):
    id: int
    name: str
    stir: str
    phone_number: str

    class ConfigDict:
        from_attributes = True


class CompanyCreate(BaseModel):
    name: str
    stir: str
    phone_number: str


class CompanyUpdate(BaseModel):
    name: str
    phone_number: str
