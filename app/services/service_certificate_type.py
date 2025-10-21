from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.certificate_type import CertificateType
from app.schemas.certificate_type import CertificateTypeCreate


class ServiceCertificateType:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_certificate_types(self):
        query = select(CertificateType)
        result = await self.db.execute(query)
        return result.scalars().all()

    async def add_certificate_type(self, certificate_type: CertificateTypeCreate):
        data = certificate_type.model_dump()
        certificate_type = CertificateType(**data)
        self.db.add(certificate_type)
        await self.db.commit()
        return certificate_type

    async def delete_certificate_type(self, certificate_type_id):
        print(certificate_type_id, 'id')
        query = select(CertificateType).where(CertificateType.id == certificate_type_id)
        result = await self.db.execute(query)
        check = result.scalar_one_or_none()
        print(result, 'result')
        print(check, 'check')