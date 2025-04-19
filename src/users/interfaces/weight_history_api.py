from fastapi import APIRouter, Depends
from src.users.schemas.user_schema import WeightHistoryOut, WeightHistoryCreate
from src.users.infrastructure.database.sql_weight_history_repository import SqlWeightHistoryRepository
from src.users.use_cases.weight_history_usecase import WeightHistoryUseCase
from src.users.domain.entities import User
from src.core.jwt.jwt import AuthService
from src.core.exceptions.response_exception import ResponseException, ResponseCodes
from tortoise.exceptions import DoesNotExist
from src.core.response.responses import OkResponse

router = APIRouter(
    prefix="/weight-history",
    tags=["weight-history"],
)

def get_usecase():
    return WeightHistoryUseCase(SqlWeightHistoryRepository())

@router.post("/", response_model=WeightHistoryOut)
async def create_weight_history(
    weight: WeightHistoryCreate,
    user: User = Depends(AuthService.get_current_user),
    use_case: WeightHistoryUseCase = Depends(get_usecase)
):
    return await use_case.create_weight_history(user.id, weight)

@router.get("/", response_model=list[WeightHistoryOut])
async def get_weight_history(
    user: User = Depends(AuthService.get_current_user),
    use_case: WeightHistoryUseCase = Depends(get_usecase)
):
    return await use_case.get_weight_history(user.id)

@router.delete("/{id}")
async def get_weight_history(
    id: int,
    user: User = Depends(AuthService.get_current_user),
    use_case: WeightHistoryUseCase = Depends(get_usecase)
):
    try:
        await use_case.delete(user.id, id)
        return OkResponse(
            message="Weight history deleted successfully",
            code=ResponseCodes.SUCCESS,
        )
    except DoesNotExist as e:
        raise ResponseException(
            e,
            message="Weight history not found",
            code=ResponseCodes.NOT_FOUND,
        )
    except Exception as e:
        raise ResponseException(
            e,
            code=ResponseCodes.UNKNOWN_ERROR,
            message="An unknown error occurred",
        )
