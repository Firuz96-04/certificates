from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException
from app.models.country import Country
from app.schemas import CountrySchema, CountryBase


class ServiceCountry:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_countries(self):
        query = select(Country)
        result = await self.db.execute(query)
        return result.scalars().all()

    async def get_by_id(self, id):
        query = select(Country).where(Country.id == id)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()

    async def add_country(self, country: CountryBase):
        # data = country.model_dump()
        # self.db.add(Country(**data))
        # await self.db.commit()
        # await self.db.refresh(data)
        # return data
        exist_data = await self.db.execute(select(Country).where(Country.name.icontains(country.name)))
        if exist_data.scalar_one_or_none():
            raise HTTPException(status_code=400, detail="country already exists")
        new_country = Country(**country.model_dump())  # создаём объект модели
        self.db.add(new_country)
        await self.db.commit()
        await self.db.refresh(new_country)  # обновляем сам объект
        return new_country

    async def update_country(self, country_id: int, country: CountryBase):
        query = await self.db.execute(select(Country).where(Country.id == country_id))
        item = query.scalar_one_or_none()
        if item is None:
            raise HTTPException(detail="country not exists", status_code=400)
        item.name = country.name
        await self.db.commit()
        await self.db.refresh(item)
        return item