
from pydantic import BaseModel, ConfigDict


class ProductCreate(BaseModel):
    name: str
    measure: str
    code: str
    winter: bool = False
    spring: bool = False
    summer: bool = False
    autumn: bool = False


class ProductUpdate(ProductCreate):
    pass


class ProductInfo(ProductCreate):
    id: int

    class ConfigDict:
        from_attributes = True
