from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import URL, create_engine, text
from config import *
import asyncio


DATABASE_URL = f"postgresql+psycopg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
DATABASE_URL_ASYNC = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

sync_engine = create_engine(
    url=DATABASE_URL,
    echo=False,
    pool_size=5,
    max_overflow=10
)

async_engine = create_async_engine(
    url=DATABASE_URL_ASYNC,
    echo=False,
    pool_size=5,
    max_overflow=10
)

with sync_engine.connect() as conn:
    res = conn.execute(text("SELECT VERSION()"))
    print(f"{res.first()=}")


async def get_123():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT VERSION()"))
        print(f"{res.first()=}")

asyncio.run(get_123())

