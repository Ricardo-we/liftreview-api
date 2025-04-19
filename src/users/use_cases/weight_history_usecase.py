
from src.users.domain.entities import  WeightHistory
from src.users.domain.repository import  WeightHistoryRepository
from src.users.schemas.user_schema import  WeightHistoryCreate
from tortoise.exceptions import DoesNotExist
from datetime import date

class WeightHistoryUseCase:
    def __init__(self, weight_history_repository: WeightHistoryRepository):
        self.weight_history_repository = weight_history_repository
        
    async def create_weight_history(self, user_id: int, weight_data: WeightHistoryCreate) -> WeightHistory:
        weight_history = WeightHistory(user_id=user_id, weight=weight_data.weight, date=date.today())
        return await self.weight_history_repository.create(weight_history)

    async def get_weight_history(self, user_id: int) -> list[WeightHistory]:
        return await self.weight_history_repository.get_by_user(user_id)
    
    
    async def delete(self, user_id: int, weight_history_id: int) -> None:
        weight_history = await self.weight_history_repository.get_by_id(weight_history_id)
        if weight_history.user_id != user_id:
            raise Exception("Unauthorized to delete this weight history.")
        
        await self.weight_history_repository.delete(weight_history)
        return None