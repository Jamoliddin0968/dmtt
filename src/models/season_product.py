# Your models for the app
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.models.base import BaseModel


class SeasonProduct(BaseModel):
    __tablename__ = 'season_products'

    id = Column(Integer, primary_key=True)
    season = Column(Integer)
    product_id = Column(Integer, ForeignKey('products.id'))

    product = relationship('Product', back_populates='season_associations')
