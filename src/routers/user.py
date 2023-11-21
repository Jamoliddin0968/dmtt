from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.schemas.user import UserCreate
from src.services.user import UserService
# from src.utils import create_access_token, create_refresh_token

router = APIRouter(prefix='/user')


@router.get("/all")
def get_all_user():
    return {"hello": "world"}


@router.post("/create")
async def create_user(data: UserCreate, db: Session = Depends(get_db)):
    if UserService.get_by_username(username=data.username, db=db):
        raise HTTPException(
            status_code=422, detail="Bu username li foydalanuvchi allaqachon mavjud"
        )
    user = await UserService.create_user(data=data, db=db)
    return user



