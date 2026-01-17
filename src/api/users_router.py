from fastapi import APIRouter

router = APIRouter(prefix = '/users')

@router.get("/{user_id}")
async def read_current_user(user_id: str):
    return {"username": user_id}