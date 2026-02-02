from datetime import datetime, timedelta
from typing import Annotated
from fastapi import Depends, HTTPException, APIRouter, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from uuid import uuid4

from src.models.user import User
from src.models.token import Token
from src.schemas.user import UserCreate
from src.services.user_service import UserService
from src.config.settings import settings

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

@router.post('/create-user', status_code=status.HTTP_201_CREATED)
async def create_user(create_user_request: UserCreate):
    try:
        await UserService.create_user(create_user_request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def create_access_token(username: str, user_id: int, expires_delta: timedelta, refresh: bool = False):
    to_encode = {
        "sub": username,
        "id": user_id,
        "exp": datetime.now() + expires_delta,
        "jti": str(uuid4()),
        "refresh": refresh
    }
    return jwt.encode(to_encode, key=settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM)

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, 
            key=settings.JWT_SECRET_KEY, 
            algorithms=[settings.ALGORITHM]
        )
        username = payload.get("sub")
        user_id = payload.get("id")
        if not username or not user_id:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await UserService.get_user_by_id(user_id)
    if user is None:
        raise credentials_exception
    return user

@router.post('/login', response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = await UserService.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        user.username, 
        user.id, 
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    refresh_token = create_access_token(
        user.username, 
        user.id, 
        expires_delta=timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS), 
        refresh=True
    )
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}