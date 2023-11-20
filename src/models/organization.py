from sqlalchemy import Boolean, Column, Integer, String

from src.models.base import BaseModel


class Organization(BaseModel):
    __tablename__ = 'organization'

    name = Column(String(255))
    phone_number = Column(String(15))
    stir = Column(String(10), nullable=True)
    tg_user_id = Column(String(10), nullable=True)
    is_active = Column(Boolean(), default=True)

    def __repr__(self):
        return f"<Organization(name='{self.name}')>"
