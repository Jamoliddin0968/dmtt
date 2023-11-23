from sqlalchemy import Boolean, Column, Integer
from sqlalchemy.orm import relationship

from src.models.base import BaseModel


class Period(BaseModel):
    __tablename__ = "period"
    start_date = Column(Integer)
    end_date = Column(Integer)
    is_active = Column(Boolean, default=False)
    year = Column(Integer)
    month = Column(Integer)

    limit = relationship('Limit', back_populates='period')
