from fastapi import APIRouter, Depends
from src.users.schemas.user_schema import WeightHistoryOut
from src.users.schemas.user_schema import WeightHistoryCreate
from src.users.infrastructure.database.sql_weight_history_repository import SqlWeightHistoryRepository
from src.users.use_cases.weight_history_usecase import WeightHistoryUseCase


router = APIRouter(prefix="/weight-history", tags=["weight-history"])

def get_usecase():
    return WeightHistoryUseCase(SqlWeightHistoryRepository())


@router.post("/{user_id}/weight_history", response_model=WeightHistoryOut)
async def create_weight_history(user_id: int, weight: WeightHistoryCreate, use_case: WeightHistoryUseCase = Depends(get_usecase)):
    return await use_case.create_weight_history(user_id, weight)

@router.get("/{user_id}/weight_history", response_model=list[WeightHistoryOut])
async def get_weight_history(user_id: int, use_case: WeightHistoryUseCase = Depends(get_usecase)):
    return await use_case.get_weight_history(user_id)