from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.dependencies import get_current_user
from src.models.user import User
from src.schemas.user import UserCreate, UserInfo
from src.services.user import UserService

# from src.utils import create_access_token, create_refresh_token

router = APIRouter(prefix='/user', tags=["user",])


@router.get("/all")
def get_all_user(user: User = Depends(get_current_user)):
    return {"hello": "world"}


@router.post("/create")
async def create_user(data: UserCreate, db: Session = Depends(get_db)):
    if UserService.get_by_username(username=data.username, db=db):
        raise HTTPException(
            status_code=422, detail="Bu username li foydalanuvchi allaqachon mavjud"
        )
    user = await UserService.create_user(data=data, db=db)
    return user


@router.get("/me", response_model=UserInfo)
def get_me(user: User = Depends(get_current_user)):
    return user
