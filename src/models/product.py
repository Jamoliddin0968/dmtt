# Your models for the app
import enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# Enum for seasons
from sqlalchemy.orm import relationship

from src.models.base import BaseModel


class Seasons(enum.Enum):
    WINTER = 0
    SUMMER = 2
    SPRING = 1
    AUTUMN = 3

# Product model


class Product(BaseModel):
    __tablename__ = 'products'
    name = Column(String(127))
    measure = Column(String(15))
    code = Column(String(31))

    season_associations = relationship(
        'SeasonProduct', back_populates='product')

# SeasonProduct association table model
