from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.database import get_db
from src.schemas.auth import AuthSchema
from src.schemas.token import TokenSchema
from src.services.auth import AuthService

router = APIRouter(prefix='/auth')


@router.post('/login')
def login(data: AuthSchema, db: Session = Depends(get_db)) -> TokenSchema:
    user = AuthService.authenticate(data, db)
    return AuthService.get_tokens(user_id=user.id)


@router.post('/swagger/login')
def login_swagger(data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = AuthService.authenticate(data, db)
    return AuthService.get_tokens(user_id=user.id)
