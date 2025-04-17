from domain.entities import User, WeightHistory
from domain.repository import UserRepository, WeightHistoryRepository
from schemas.user_schema import UserCreate, UserOut, WeightHistoryCreate
from tortoise.exceptions import DoesNotExist
from datetime import date

class UserUseCase:
    def __init__(self, user_repo: UserRepository, weight_history_repo: WeightHistoryRepository):
        self.user_repo = user_repo
        self.weight_history_repo = weight_history_repo

    # Crear usuario
    async def create_user(self, user_data: UserCreate) -> UserOut:
        user = User(name=user_data.name, email=user_data.email, phone=user_data.phone,
                    age=user_data.age, height=user_data.height, gender=user_data.gender)
        created_user = await self.user_repo.create(user)
        return UserOut.from_orm(created_user)

    # Obtener usuario por ID
    async def get_user(self, user_id: int) -> UserOut:
        try:
            user = await self.user_repo.get(user_id)
            return UserOut.from_orm(user)
        except DoesNotExist:
            raise ValueError("User not found")

    # Crear historial de peso
    async def create_weight_history(self, user_id: int, weight_data: WeightHistoryCreate) -> WeightHistory:
        weight_history = WeightHistory(user_id=user_id, weight=weight_data.weight, date=date.today())
        return await self.weight_history_repo.create(weight_history)

    # Obtener historial de peso por usuario
    async def get_weight_history(self, user_id: int) -> list[WeightHistory]:
        return await self.weight_history_repo.get_by_user(user_id)
