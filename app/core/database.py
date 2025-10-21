from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from .config import settings


class Base(DeclarativeBase):
    pass


async_engine = create_async_engine(
    url=settings.database.async_connection,
    echo=settings.ECHO
)

async_session_factory = async_sessionmaker(
    async_engine,
    expire_on_commit=False,
    autoflush=False,
    autocommit=False,
    class_=AsyncSession,
)


async def get_async_db():
    async with async_session_factory() as session:
        yield session
