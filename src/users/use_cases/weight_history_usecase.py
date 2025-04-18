
from src.users.domain.entities import  WeightHistory
from src.users.domain.repository import  WeightHistoryRepository
from src.users.schemas.user_schema import  WeightHistoryCreate
from tortoise.exceptions import DoesNotExist
from datetime import date

class WeightHistoryUseCase:
    def __init__(self, weight_history_repository: WeightHistoryRepository):
        self.weight_history_repository = weight_history_repository
        
    # Crear historial de peso
    async def create_weight_history(self, user_id: int, weight_data: WeightHistoryCreate) -> WeightHistory:
        weight_history = WeightHistory(user_id=user_id, weight=weight_data.weight, date=date.today())
        return await self.weight_history_repo.create(weight_history)

    # Obtener historial de peso por usuario
    async def get_weight_history(self, user_id: int) -> list[WeightHistory]:
        return await self.weight_history_repo.get_by_user(user_id)
    