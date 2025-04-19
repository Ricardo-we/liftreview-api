

from src.users.domain.entities import  WeightHistory
from src.users.domain.repository import  WeightHistoryRepository
from src.users.infrastructure.database.models import  WeightHistoryModel


class SqlWeightHistoryRepository(WeightHistoryRepository):
    async def get_by_user(self, user_id: int) -> list[WeightHistory]:
        histories = await WeightHistoryModel.filter(user_id=user_id).all()
        return [history.to_domain() for history in histories]
    
    async def create(self, weight_history: WeightHistory) -> WeightHistory:
        weight_history_model = WeightHistoryModel(user_id=weight_history.user_id, weight=weight_history.weight,
                                                  date=weight_history.date)
        await weight_history_model.save()
        return weight_history_model.to_domain()
    
    async def delete(self, weight_history: WeightHistory) -> None:
        weight_history_model = await WeightHistoryModel.get(id=weight_history.id)
        await weight_history_model.delete()
        
    async def get_by_id(self, weight_history_id: int) -> WeightHistory:
        weight_history_model = await WeightHistoryModel.get(id=weight_history_id)
        return weight_history_model.to_domain()
    