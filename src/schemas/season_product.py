from pydantic import BaseModel, ConfigDict, Field


class SeasonProductBase(BaseModel):
    season: int = Field(ge=0, le=3)
    product_id: int


class SeasonProductCreate(SeasonProductBase):
    pass


class SeasonProductUpdate(SeasonProductBase):
    pass


class SeasonProductInfo(SeasonProductBase):
    id: int

    class ConfigDict:
        from_attributes = True
