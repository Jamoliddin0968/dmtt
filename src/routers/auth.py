from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.schemas.auth import AuthSchema
from src.services.auth import AuthService

router = APIRouter(prefix='/auth')


@router.post('/login')
def login(data: AuthSchema, db: Session = Depends(get_db)):
    user = AuthService.authenticate(data, db)
    if not user:
        raise HTTPException(
            status_code=422, detail="mumkinbas sizga ")
    return AuthService.get_tokens(user_id=user.id)