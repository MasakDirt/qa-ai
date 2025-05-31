from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from backend.src.configs.internal.database import PostgresConfig


def get_db_url() -> str:
    return PostgresConfig().async_db_uri


engine = create_async_engine(
    get_db_url(),
    echo=False,
    future=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
    autocommit=False
)


async def get_db() -> AsyncSession:
    async with SessionLocal() as session:
        yield session
