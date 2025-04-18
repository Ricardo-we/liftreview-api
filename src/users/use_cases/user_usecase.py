from src.users.domain.entities import User
from src.users.domain.repository import UserRepository
from tortoise.exceptions import DoesNotExist
import bcrypt
from src.users.schemas.user_schema import UserCreate

class UserUseCase:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def create_user(self, user_data: UserCreate) -> User:
        hashed_password = bcrypt.hashpw(user_data.password.encode(), bcrypt.gensalt()).decode()
        user = User(
            name=user_data.name, 
            email=user_data.email, 
            phone=user_data.phone,
            age=user_data.age, 
            height=user_data.height, 
            gender=user_data.gender,
            password=hashed_password
        )
        created_user = await self.user_repo.create(user)
        return created_user

    async def login(self, email: str, password: str) -> User:
        try:
            user = await self.user_repo.get_by_email(email)
            if not user:
                return None
            
            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return user
            return None
        except DoesNotExist:
            print(f"Usuario con correo {email} no encontrado.")
            return None
        except Exception as e:
            print(f"Error durante login: {e}")
            return None