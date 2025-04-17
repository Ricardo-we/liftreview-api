from typing import Optional
from pydantic import BaseModel
from datetime import date

# Entidad de Usuario
class User(BaseModel):
    id: Optional[int]
    name: str
    email: str
    phone: Optional[str] = None
    age: Optional[int] = None
    height: Optional[float] = None
    gender: Optional[str] = None

# Entidad Historial de Peso
class WeightHistory(BaseModel):
    id: Optional[int]
    user_id: int
    weight: float
    date: date
