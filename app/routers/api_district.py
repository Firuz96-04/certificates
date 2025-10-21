from fastapi import APIRouter, Depends
from app.core.database import get_async_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.service_distirct import ServiceDistrict

router = APIRouter(prefix='/district', tags=['Districts'])


@router.get('/')
async def get_districts(db: AsyncSession = Depends(get_async_db)):
    result = await ServiceDistrict(db).get_all_districts()
    return result
