from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from src.models.base import BaseModel


class Company(BaseModel):
    __tablename__ = 'company'

    name = Column(String(255))
    phone_number = Column(String(15))
    stir = Column(String(10), nullable=True)
    tg_user_id = Column(String(10), nullable=True)
    is_active = Column(Boolean(), default=True)

    connect_company = relationship(
        'Connection', back_populates='company')

    limit = relationship('Limit', back_populates='company')

    def __repr__(self):
        return f"<Company(name='{self.name}')>"
