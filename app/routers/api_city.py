from fastapi import APIRouter, Depends
from app.core.database import get_async_db
from app.models import City
from app.schemas.city import CityCreate, CityRead
from typing import List
# from pydantic import
from app.services.service_city import ServiceCity
router = APIRouter(prefix="/cities", tags=["city"])


@router.get('/')
async def cities(db=Depends(get_async_db)):
    cities = await ServiceCity(db).get_cities()
    # test = [CityRead.model_validate(cities).model_dump()]
    # result = [CityRead.model_validate(city).model_dump() for city in cities]
    return cities
    # print(cities)
    # return cities


@router.post("/add")
async def city_add(city: CityCreate, db=Depends(get_async_db)):
    service = await ServiceCity(db).add_city(city)
    return {"data": service}