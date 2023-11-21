from sqlalchemy import Boolean, Column, Integer, String

# from src.dependencies import hashing
from src.models.base import BaseModel


class User(BaseModel):
    __tablename__ = "users"
    name = Column(String(50))
    username = Column(String(31))
    password = Column(String(255))
    is_admin = Column(Boolean, default=False)
    is_super_admin = Column(Boolean, default=False)
