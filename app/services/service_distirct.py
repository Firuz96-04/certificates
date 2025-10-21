from app.core.database import get_async_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.models import District


class ServiceDistrict:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all_districts(self):
        query = select(District).options(selectinload(District.city))
        result = await self.db.execute(query)
        return result.scalars().all()
