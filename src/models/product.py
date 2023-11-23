from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.models.base import BaseModel


class Product(BaseModel):
    __tablename__ = 'products'
    name = Column(String(127))
    measure = Column(String(15))
    code = Column(String(31))
    winter = Column(Boolean, default=False)
    spring = Column(Boolean, default=False)
    summer = Column(Boolean, default=False)
    autumn = Column(Boolean, default=False)

    connect_products = relationship(
        'Connection', back_populates='product')

    limit_item = relationship('LimitItem', back_populates='product')
