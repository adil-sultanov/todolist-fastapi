from src.models.user import User
from src.schemas.user import UserChangePassword, UserCreate, UserUpdate
from src.repositories.user_repo import UserRepository
from src.security import hash_password, verify_password
from src.exceptions import UserNotFound, InvalidPassword

class UserService:
    @staticmethod
    async def get_user_by_id(user_id: int) -> User | None:
        user = await UserRepository.get_by_id(user_id)
        return user

    @staticmethod
    async def get_user_by_username(username: str) -> User | None:
        user = await UserRepository.get_by_username(username)
        if not user:
            return None
        return user
    
    @staticmethod
    async def update_user(user_id: int, user_data: UserUpdate) -> User | None:
        user = await UserRepository.get_by_id(user_id)
        if not user:
            return None
        
        return await UserRepository.update(user, user_data.model_dump(exclude_unset=True))

    @staticmethod
    async def change_password(user_id: int, password_data: UserChangePassword) -> None:
        user = await UserRepository.get_by_id(user_id)
        if not user:
            raise UserNotFound()
        
        if not verify_password(password_data.current_password, user.hashed_password):
            raise InvalidPassword()
        
        update_dict = {"hashed_password": hash_password(password_data.new_password)}
        await UserRepository.update(user, update_dict)

    @staticmethod
    async def create_user(user_create: UserCreate) -> User:
        try:
            user = await UserRepository.create({
                "username": user_create.username,
                "name": user_create.name,
                "email": user_create.email,
                "age": user_create.age,
                "hashed_password": hash_password(user_create.password)
            })
            return user
        except Exception as e:
            raise e
    
    @staticmethod
    async def authenticate_user(username: str, password: str) -> User | None:
        user = await UserRepository.get_by_username(username)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user