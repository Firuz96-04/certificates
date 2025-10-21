from fastapi import Depends
from app.core.database import get_async_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.certificate_theme import CertificateTheme
from sqlalchemy import select


class CertificateThemeService:

    def __str__(self, db: AsyncSession = Depends(get_async_db)):
        self.db = db

    async def get_certificate_themes(self):
        query = select(CertificateTheme)
        result = await self.db.execute(query)
        return result.scalars().all()
