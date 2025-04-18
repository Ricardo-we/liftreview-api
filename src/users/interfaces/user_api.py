from fastapi import APIRouter, Depends
from src.users.use_cases.user_usecase import UserUseCase
from src.users.schemas.user_schema import UserCreate, UserLogin
from src.users.infrastructure.database.sql_user_repository import SqlUserRepository
from src.users.infrastructure.database.sql_user_repository import SqlUserRepository
from src.users.domain.entities import User
from src.users.infrastructure.database.sql_weight_history_repository import (
    SqlWeightHistoryRepository)

router = APIRouter(prefix="/users", tags=["users"])

def get_usecase() -> UserUseCase:
    return UserUseCase(SqlUserRepository(), SqlWeightHistoryRepository())

@router.post("/")
async def create_user(user: UserCreate, use_case: UserUseCase = Depends(get_usecase)):
    return await use_case.create_user(user)

@router.post("/login")
async def get_user(user: UserLogin, use_case: UserUseCase = Depends(get_usecase)):
    return await use_case.login(user.email, user.password)


