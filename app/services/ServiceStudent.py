from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models import Student


class ServiceStudent:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_students(self):
        smtm = select(Student)
        query = await self.db.execute(smtm)
        result = query.scalars().all()
        return result

    async def add_student(self):
        pass