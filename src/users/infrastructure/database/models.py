from tortoise import fields
from tortoise.models import Model
from src.users.domain.entities import User, WeightHistory

# Modelo Tortoise para Usuario
class UserModel(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=255, unique=True)
    phone = fields.CharField(max_length=15, null=True)
    age = fields.IntField(null=True)
    height = fields.FloatField(null=True)
    gender = fields.CharField(max_length=10, null=True)
    password = fields.CharField(max_length=300)

    def to_domain(self) -> User:
        return User(
            id=self.id,
            name=self.name,
            email=self.email,
            phone=self.phone,
            age=self.age,
            height=self.height,
            gender=self.gender,
            password=self.password,
            weight_history=[
                wh.to_domain() for wh in self.weight_history
            ] if hasattr(self, "weight_history") else []
        )

class WeightHistoryModel(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.UserModel", related_name="weight_histories", on_delete=fields.CASCADE)
    weight = fields.FloatField()
    date = fields.DateField()

    def to_domain(self) -> WeightHistory:
        return WeightHistory(
            id=self.id,
            user_id=self.user_id,
            weight=self.weight,
            date=self.date
        )
