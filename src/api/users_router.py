from fastapi import APIRouter
from src.databases.models.user import User

router = APIRouter(prefix = '/users')

@router.get("/{user_id}")
async def get_user(user_id: str):
    user = await User.get(id=user_id)
    return user