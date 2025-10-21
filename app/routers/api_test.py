from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.city import City
from sqlalchemy import select
from sqlalchemy.orm import selectinload, defer
from app.core.database import get_async_db
from app.schemas.city import CityCreate

router = APIRouter(prefix='/test', tags=['Test Api`s'])


@router.get("/")
async def main_test(db: AsyncSession = Depends(get_async_db)):
    smtm = (
        select(City)
        .options(
            selectinload(City.country),  # подгружаем связанную страну
            defer(City.country_id)
        )
    )
    query = await db.execute(smtm)
    result = query.scalars().all()
    print(result)
    return result


@router.post("/")
async def test_add(city: CityCreate, db: AsyncSession = Depends(get_async_db)):
    dmb = city.model_dump()
    query = City(**dmb)
    db.add(query)
    await db.commit()
    await db.refresh(query)
    return "add"
