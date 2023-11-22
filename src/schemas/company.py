from pydantic import BaseModel, ConfigDict, EmailStr


class CompanyInfo(BaseModel):
    name: str
    stir: str
    phone_number: str

    class ConfigDict:
        from_attributes = True


class CompanyCreate(CompanyInfo):
    name: str
    stir: str
    phone_number: str


class CompanyUpdate(BaseModel):
    name: str
    phone_number: str
