from sqlalchemy.orm import Session

from src.models.user import User
from src.utils import (create_access_token, create_refresh_token,
                       verify_password)


class AuthService:

    @staticmethod
    def authenticate(data, db):
        username, password = data.username, data.password
        user = db.query(User).filter(User.username == username).first()
        if user and verify_password(password=password, hashed_pass=user.password):
            return user
        return None

    @staticmethod
    def get_tokens(user_id):
        return {
            "access_token": create_access_token(user_id),
            "refresh_token": create_refresh_token(user_id)
        }

    @staticmethod
    def get_user_by_id(user_id, db):
        return db.query(User).filter(User.id == user_id).first()
