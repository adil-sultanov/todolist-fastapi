from fastapi import APIRouter, HTTPException

from src.services.user_service import UserService
from src.schemas.user import UserOut, UserCreate

router = APIRouter(prefix = '/users')

@router.get('/{user_id}', response_model=UserOut)
async def get_user(user_id: int):
    user = await UserService.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserOut.from_orm(user)

@router.post('/', response_model=UserOut)
async def create_user(user_create: UserCreate):
    user = await UserService.create_user(user_create)
    return UserOut.from_orm(user)