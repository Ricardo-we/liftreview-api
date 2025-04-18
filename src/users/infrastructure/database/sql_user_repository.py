from src.users.domain.entities import User, WeightHistory
from src.users.domain.repository import UserRepository, WeightHistoryRepository
from src.users.infrastructure.database.models import UserModel, WeightHistoryModel

class SqlUserRepository(UserRepository):
    async def create(self, user: User) -> User:
        user_model = UserModel(
            name=user.name, 
            email=user.email, 
            phone=user.phone, 
            age=user.age,
            height=user.height, 
            gender=user.gender,
            password=user.password
        )
        
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

    async def get_by_email(self, email: str) -> User:
        user_model = await UserModel.get(email=email).prefetch_related("weight_histories")
        return user_model.to_domain()
    
    async def get_weight_history(self, user_id: int) -> list[WeightHistory]:
        weight_history_models = await WeightHistoryModel.filter(user_id=user_id).all()
        return [weight_history_model.to_domain() for weight_history_model in weight_history_models]
    