from typing import List

from pydantic import BaseModel, ConfigDict


class LimitItem(BaseModel):
    product_id: int
    count: float


class Limit(BaseModel):
    dmtt_id: int
    items: List[LimitItem]
