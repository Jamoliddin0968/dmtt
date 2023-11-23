from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from src.models.base import BaseModel


class Dmtt(BaseModel):
    __tablename__ = 'dmtt'

    name = Column(String(255))
    person = Column(String(63))
    phone_number = Column(String(15))
    address = Column(String(127), nullable=True)
    stir = Column(String(10), nullable=True)
    tg_user_id = Column(String(10), nullable=True)
    is_active = Column(Boolean(), default=True)

    connect_dmtt = relationship(
        'Connection', back_populates='dmtt')
    limit = relationship('Limit', back_populates='dmtt')

    def __repr__(self):
        return f"<dmtt(name='{self.name}')>"
