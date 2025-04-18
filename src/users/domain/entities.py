# src/users/domain/entities.py
from dataclasses import dataclass
from typing import Optional
from datetime import date

@dataclass
class User:
    name: str
    email: str
    id: Optional[int] = None
    phone: Optional[str] = None
    age: Optional[int] = None
    height: Optional[float] = None
    gender: Optional[str] = None
    password: Optional[str] = None

@dataclass
class WeightHistory:
    user_id: int
    weight: float
    date: date
    id: Optional[int] = None
