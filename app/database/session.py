from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from configuration.config import settings
from sqlalchemy.orm import sessionmaker

DATABASE_URL = f'postgresql+asyncpg://{settings.database_user}:{settings.database_pass}@{settings.database_host}:{settings.database_port}/{settings.database_name}'

engine = create_async_engine(url=DATABASE_URL, echo=False)

SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def get_db():
    async with SessionLocal() as session:
        yield session
