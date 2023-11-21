
from pydantic import BaseModel, ConfigDict


# Pydantic schemas for Product and SeasonProduct models
class ProductBase(BaseModel):
    name: str
    measure: str
    code: str


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductInfo(ProductBase):
    id: int

    class ConfigDict:
        from_attributes = True


# Additional schemas if needed
