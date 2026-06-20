from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator

from app.core.db_init import async_session


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session