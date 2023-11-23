# Your models for the app
import enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.models.base import BaseModel


class Seasons(enum.Enum):
    WINTER = 0
    SUMMER = 2
    SPRING = 1
    AUTUMN = 3


class Product(BaseModel):
    __tablename__ = 'products'
    name = Column(String(127))
    measure = Column(String(15))
    code = Column(String(31))

    season_associations = relationship(
        'SeasonProduct', back_populates='product')

    connect_products = relationship(
        'Connection', back_populates='product')

    limit_item = relationship('LimitItem', back_populates='product')
