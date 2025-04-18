import datetime
from src.users.domain.entities import User, WeightHistory
from src.users.domain.repository import UserRepository, WeightHistoryRepository
from tortoise.exceptions import DoesNotExist
import bcrypt
from src.users.schemas.user_schema import UserCreate
from src.core.jwt.jwt import AuthService

class UserUseCase:
    def __init__(self, user_repo: UserRepository,weight_history_repo: WeightHistoryRepository):
        self.weight_history_repo = weight_history_repo
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
        create_weight_history = await self.weight_history_repo.create(
            WeightHistory(user_id=created_user.id, weight=user_data.weight, date=datetime.date.today())
        )
        
        created_user.weight_history = [create_weight_history]
        return created_user

    async def login(self, email: str, password: str) -> dict | None:
        try:
            user = await self.user_repo.get_by_email(email)
            if not user:
                return None

            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                token = AuthService.create_access_token({
                    "user_id": user.id,
                    "email": user.email,
                    "name": user.name,
                    "phone": user.phone,
                    "age": user.age,
                })
                return {
                    "user": user,
                    "access_token": token,
                    "token_type": "bearer"
                }

            return None
        except DoesNotExist:
            print(f"Usuario con correo {email} no encontrado.")
            return None
        except Exception as e:
            print(f"Error durante login: {e}")
            return None