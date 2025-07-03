from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import asynccontextmanager
from .config import settings

DATABASE_URL = settings.DB_ASYNC_URL

# Async engine for PostgreSQL
engine = create_async_engine(DATABASE_URL, echo=True, future=True)
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

# PUBLIC_INTERFACE
@asynccontextmanager
async def get_db():
    """Yields a db session for dependency injection in FastAPI endpoints."""
    async with AsyncSessionLocal() as session:
        yield session
