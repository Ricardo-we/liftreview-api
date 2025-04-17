from domain.entities import User, WeightHistory
from domain.repository import UserRepository, WeightHistoryRepository
from user_model import UserModel, WeightHistoryModel

class TortoiseUserRepository(UserRepository):
    async def create(self, user: User) -> User:
        user_model = UserModel(name=user.name, email=user.email, phone=user.phone, age=user.age,
                               height=user.height, gender=user.gender)
        await user_model.save()
        return user_model.to_domain()

    async def get(self, user_id: int) -> User:
        user_model = await UserModel.get(id=user_id)
        return user_model.to_domain()

    async def update(self, user: User) -> User:
        user_model = await UserModel.get(id=user.id)
        user_model.name = user.name
        user_model.email = user.email
        user_model.phone = user.phone
        user_model.age = user.age
        user_model.height = user.height
        user_model.gender = user.gender
        await user_model.save()
        return user_model.to_domain()

    async def delete(self, user: User) -> None:
        await UserModel.filter(id=user.id).delete()

# Implementación de Repositorio para Historial de Peso
class TortoiseWeightHistoryRepository(WeightHistoryRepository):
    async def create(self, weight_history: WeightHistory) -> WeightHistory:
        weight_history_model = WeightHistoryModel(user_id=weight_history.user_id, weight=weight_history.weight,
                                                  date=weight_history.date)
        await weight_history_model.save()
        return weight_history_model.to_domain()

    async def get_by_user(self, user_id: int) -> list[WeightHistory]:
        histories = await WeightHistoryModel.filter(user_id=user_id).all()
        return [history.to_domain() for history in histories]