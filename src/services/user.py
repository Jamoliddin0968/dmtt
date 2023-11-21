from src.models.user import User
from src.utils import get_hashed_password


class UserService:
    @staticmethod
    async def create_user(data, db):
        data = data.dict()
        pswd = data.pop('password')
        user = User(**data)
        user.password = get_hashed_password(pswd)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def get_by_username(username, db):
        return db.query(User).filter(User.username == username).first()
