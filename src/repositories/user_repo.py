from sqlite3 import IntegrityError
from src.models.user import User

class UserRepository:
    @staticmethod
    async def get_by_id(user_id: int) -> User | None:
        return await User.get(id=user_id)

    @staticmethod
    async def get_by_username(username: str) -> User | None:
        return await User.get_or_none(username=username)

    @staticmethod
    async def create(data: dict) -> User:
        try:
            user = await User.create(**data)
            return user
        except IntegrityError:
            raise ValueError("User with this email already exists")

    @staticmethod
    async def update(user: User, data: dict) -> User:
        user.update_from_dict(data)
        await user.save()
        return user