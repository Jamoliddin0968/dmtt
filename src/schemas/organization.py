from pydantic import BaseModel, EmailStr


class CompanyInfo(BaseModel):
    name: str
    stir: str
    phone_number: str


class OrganizationCreate(CompanyInfo):
    pass


class OrganizationUpdate(BaseModel):
    name: str
    phone_number: str
