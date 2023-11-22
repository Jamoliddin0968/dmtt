from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.models.base import BaseModel


class Connection(BaseModel):
    __tablename__ = "connection"

    product_id = Column(Integer, ForeignKey('products.id', ondelete='CASCADE'))
    company_id = Column(Integer, ForeignKey('company.id', ondelete='CASCADE'))
    dmtt_id = Column(Integer, ForeignKey('dmtt.id', ondelete='CASCADE'))

    dmtt = relationship('Dmtt', back_populates='connect_dmtt')
    company = relationship('Company', back_populates='connect_company')
    product = relationship('Product', back_populates='connect_products')
