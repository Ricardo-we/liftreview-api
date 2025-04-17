from fastapi import APIRouter, Depends
from schemas.user_schema import UserCreate, UserOut
from use_cases.create_user import CreateUser
from infrastructure.repository_psql_impl import SQLAlchemyUserRepository
from database import get_async_session

router = APIRouter()

@router.post("/users", response_model=UserOut)
async def create_user(user: UserCreate, session = Depends(get_async_session)):
    repo = SQLAlchemyUserRepository(session)
    use_case = CreateUser(repo)
    return await use_case.execute(user.name, user.email)
