from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException

from src.models.user import User
from src.services.user_service import UserService
from src.schemas.user import UserChangePassword, UserOut, UserCreate, UserUpdate
from src.exceptions import UserNotFound, InvalidPassword
from src.auth import get_current_user

router = APIRouter(prefix = '/users')
    
user_dependency = Annotated[User, Depends(get_current_user)]

@router.get('/me', response_model=UserOut)
async def get_current_user_info(user: user_dependency):
    if not user:
        raise HTTPException(status_code=401, detail="Authentication failed")
    return UserOut.model_validate(user)

@router.get('/{user_id}', response_model=UserOut)
async def get_user_by_id(user_id: int):
    user = await UserService.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserOut.model_validate(user)

@router.put('/{user_id}', response_model=UserOut)
async def update_user(user_id: int, user_data: UserUpdate):
    user = await UserService.update_user(user_id, user_data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserOut.model_validate(user)

@router.patch('/{user_id}/change-password', status_code=204)
async def change_password(user_id: int, password_data: UserChangePassword):
    try:
        await UserService.change_password(user_id, password_data)
    except UserNotFound:
        raise HTTPException(status_code=404, detail="User not found")
    except InvalidPassword:
        raise HTTPException(status_code=400, detail="Invalid current password")