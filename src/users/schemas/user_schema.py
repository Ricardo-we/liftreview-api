from pydantic import BaseModel
from typing import Optional
from datetime import date

# Esquema para la creación de un usuario
class UserCreate(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    age: Optional[int] = None
    height: Optional[float] = None
    gender: Optional[str] = None
    password: Optional[str] = None
    weight: Optional[float] = None

class UserLogin(BaseModel):
    email: str
    password: str
class WeightHistoryCreate(BaseModel):
    weight: float

class WeightHistoryOut(BaseModel):
    id: int
    user_id: int
    weight: float
    date: date

    class Config:
        orm_mode = True
