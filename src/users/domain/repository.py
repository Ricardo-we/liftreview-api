from abc import ABC, abstractmethod
from typing import List
from src.users.domain.entities import User, WeightHistory

# Interfaz de repositorio para el Usuario
class UserRepository(ABC):
    @abstractmethod
    async def create(self, user: User) -> User:
        pass

    @abstractmethod
    async def get(self, user_id: int) -> User:
        pass

    @abstractmethod
    async def update(self, user: User) -> User:
        pass
    
    @abstractmethod
    async def get_by_email(self, email: str) -> User:
        pass
    
# Interfaz de repositorio para el Historial de Peso
class WeightHistoryRepository(ABC):
    @abstractmethod
    async def create(self, weight_history: WeightHistory) -> WeightHistory:
        pass

    @abstractmethod
    async def get_by_user(self, user_id: int) -> List[WeightHistory]:
        pass
