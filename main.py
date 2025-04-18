from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from src.users.interfaces.user_api import router as user_router
from src.users.interfaces.weight_history_api import router as weight_history_router

app = FastAPI()

app.include_router(
    user_router
)
app.include_router(
    weight_history_router
)

register_tortoise(
    app,
    db_url="postgres://postgres:password@localhost:5432/liftreview",
    modules={
        "models": ["src.users.infrastructure.database.models"],
    },
    # generate_schemas=True,
    add_exception_handlers=True,
    
)


TORTOISE_ORM = {
    "connections": {
        "default": "postgres://postgres:password@localhost:5432/liftreview"
    },
    "apps": {
        "models": {
            "models": ["src.users.infrastructure.database.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
