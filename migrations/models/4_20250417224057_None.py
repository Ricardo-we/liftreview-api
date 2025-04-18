from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "usermodel" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(100) NOT NULL,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "phone" VARCHAR(15),
    "age" INT,
    "height" DOUBLE PRECISION,
    "gender" VARCHAR(10),
    "password" VARCHAR(300) NOT NULL
);
CREATE TABLE IF NOT EXISTS "weighthistorymodel" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "weight" DOUBLE PRECISION NOT NULL,
    "date" DATE NOT NULL,
    "user_id" INT NOT NULL REFERENCES "usermodel" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
