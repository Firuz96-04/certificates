from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload, defer
from starlette import status

from app.models.city import City
from app.schemas.city import CityCreate


class ServiceCity:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_cities(self):
        query = select(City).options(selectinload(City.country), defer(City.country_id))
        result = await self.db.execute(query)
        return result.scalars().all()

    async def add_city(self, city: CityCreate):
        json = city.model_dump()
        data = City(**json)
        try:
            self.db.add(data)
            await self.db.commit()
            return data
        except Exception as e:
            await self.db.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Неизвестная ошибка: {str(e)}"
            )
