from fastapi import APIRouter
from starlette import status

from app.services.service_country import ServiceCountry
from fastapi import Depends
from app.core.database import get_async_db
from app.schemas import CountryListSchema, CountrySchema, CountryBase
from typing import List
router = APIRouter(prefix='/country', tags=['Country'])


@router.get("/countries", response_model=CountryListSchema)
async def all_countries(db=Depends(get_async_db)):
    print("good")
    service = await ServiceCountry(db).get_countries()
    return {
        "data": service,
        "total": len(service)
    }


@router.get("/countries/{country_id}")
async def country_by_id(country_id: int, db=Depends(get_async_db)):
    print("good")
    service = await ServiceCountry(db).get_by_id(country_id)
    return {"data": service}


@router.post("/countries", status_code=status.HTTP_201_CREATED)
async def country_add(data: CountryBase, db=Depends(get_async_db)):
    service = await ServiceCountry(db).add_country(data)
    print(service.id)
    return {"data": service}


@router.patch("/countries/{country_id}")
async def country_update(country_id: int, data: CountryBase, db=Depends(get_async_db)):
    item = await ServiceCountry(db).update_country(country_id, data)
    print(item, 'item')
    return item