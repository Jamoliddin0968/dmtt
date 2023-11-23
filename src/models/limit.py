from sqlalchemy import (DOUBLE, Boolean, Column, Float, ForeignKey, Integer,
                        String)
from sqlalchemy.orm import relationship

from src.models.base import BaseModel


class Limit(BaseModel):
    __tablename__ = "limit"
    name = Column(String(255))

    company_id = Column(Integer, ForeignKey('company.id', ondelete='CASCADE'))
    dmtt_id = Column(Integer, ForeignKey('dmtt.id', ondelete='CASCADE'))
    period_id = Column(Integer, ForeignKey('period.id', ondelete='CASCADE'))

    period = relationship('Period', back_populates='limit')
    dmtt = relationship('Dmtt', back_populates='limit')
    company = relationship('Company', back_populates='limit')
    limit_item = relationship("LimitItem", back_populates="limit")


class LimitItem(BaseModel):
    __tablename__ = "limit_item"

    count = Column(Float, default=0)
    limit_id = Column(Integer, ForeignKey('limit.id', ondelete='CASCADE'))
    product_id = Column(Integer, ForeignKey('products.id', ondelete='CASCADE'))

    product = relationship('Product', back_populates='limit_item')
    limit = relationship('Limit', back_populates='limit_item')
