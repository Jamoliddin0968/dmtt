from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.models.base import BaseModel


class Dmtt(BaseModel):
    __tablename__ = 'dmtt'

    name = Column(String(255))
    phone_number = Column(String(15))
    address = Column(String(127), nullable=True)
    stir = Column(String(10), nullable=True)
    child_count = Column(Integer)
    is_active = Column(Boolean(), default=True)

    connect_dmtt = relationship(
        'Connection', back_populates='dmtt')
    limit = relationship('Limit', back_populates='dmtt')

    persons = relationship('Person')

    def __repr__(self):
        return f"<dmtt(name='{self.name}')>"


ZAVHOZ = 1
DIRECTOR = 2
GUARD = 3


class Person(BaseModel):
    __tablename__ = "dmtt_persons"
    dmtt_id = Column(Integer, ForeignKey('dmtt.id', ondelete='CASCADE'))
    first_name = Column(String(31))
    last_name = Column(String(31))
    phone_number = Column(String(15))
    rank = Column(Integer, default=2)
    tg_user_id = Column(String(10), nullable=True)
