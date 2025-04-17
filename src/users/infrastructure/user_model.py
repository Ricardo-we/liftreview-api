from tortoise import fields
from tortoise.models import Model
from domain.entities import User, WeightHistory
from domain.repository import UserRepository, WeightHistoryRepository
from tortoise.exceptions import DoesNotExist

# Modelo Tortoise para Usuario
class UserModel(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100)
    phone = fields.CharField(max_length=15, null=True)
    age = fields.IntField(null=True)
    height = fields.FloatField(null=True)
    gender = fields.CharField(max_length=10, null=True)

    def to_domain(self) -> User:
        return User(id=self.id, name=self.name, email=self.email, phone=self.phone,
                    age=self.age, height=self.height, gender=self.gender)

# Modelo Tortoise para Historial de Peso
class WeightHistoryModel(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.UserModel", related_name="weight_histories")
    weight = fields.FloatField()
    date = fields.DateField()

    def to_domain(self) -> WeightHistory:
        return WeightHistory(id=self.id, user_id=self.user.id, weight=self.weight, date=self.date)
