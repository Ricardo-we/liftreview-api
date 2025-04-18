from fastapi import APIRouter, Depends
from src.users.schemas.user_schema import WeightHistoryOut
from src.users.schemas.user_schema import WeightHistoryCreate
from src.users.infrastructure.database.sql_weight_history_repository import SqlWeightHistoryRepository
from src.users.use_cases.weight_history_usecase import WeightHistoryUseCase
from src.users.domain.entities import User
from src.core.jwt.jwt import AuthService


router = APIRouter(prefix="/weight-history", tags=["weight-history"])

def get_usecase():
    return WeightHistoryUseCase(SqlWeightHistoryRepository())

@router.post("/", response_model=WeightHistoryOut)
async def create_weight_history(weight: WeightHistoryCreate, user: User = Depends(AuthService.get_current_user), use_case: WeightHistoryUseCase = Depends(get_usecase)):
    return await use_case.create_weight_history(user.id, weight)

# Ruta para obtener el historial de peso del usuario
@router.get("/", response_model=list[WeightHistoryOut])
async def get_weight_history(user: User = Depends(AuthService.get_current_user), use_case: WeightHistoryUseCase = Depends(get_usecase)):
    return await use_case.get_weight_history(user.id)