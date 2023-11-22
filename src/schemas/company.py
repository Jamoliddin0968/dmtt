from pydantic import BaseModel, EmailStr


class CompanyInfo(BaseModel):
    name: str
    stir: str
    phone_number: str


class CompanyCreate(CompanyInfo):
    pass


class CompanyUpdate(BaseModel):
    name: str
    phone_number: str
