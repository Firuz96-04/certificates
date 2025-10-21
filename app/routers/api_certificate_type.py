from fastapi import APIRouter, Depends
from app.core.database import get_async_db
from app.services.service_certificate_type import ServiceCertificateType
from app.schemas.certificate_type import CertificateTypeCreate, CertificateTypeUpdate

router = APIRouter(prefix="/certificate-types", tags=["Certificate Type"])


@router.get("/")
async def get_certificate_types(db=Depends(get_async_db)):
    response = await ServiceCertificateType(db).get_certificate_types()
    return response


@router.post("/")
async def add_certificate_type(data: CertificateTypeCreate, db=Depends(get_async_db)):
    response = await ServiceCertificateType(db).add_certificate_type(data)
    print(response, 'response')
    return response


@router.patch("/{type_id}")
async def update_certificate_type(type_id: int, data: CertificateTypeUpdate, db=Depends(get_async_db)):
    print(type_id)
    print(data)


@router.delete("/{type_id}")
async def delete_certificate_type(type_id: int, db=Depends(get_async_db)):
    print(type_id, 'id')
    await ServiceCertificateType(db).delete_certificate_type(type_id)
