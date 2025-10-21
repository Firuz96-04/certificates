from sqlalchemy import SmallInteger, Integer, String
from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base


class Nationality(Base):

    __tablename__ = 'nationalities'

    id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(40))
    students: Mapped[List["Student"]] = relationship("Student", back_populates="nationality")

    def __str__(self) -> str:
        return self.name

    def __repr__(self):
        return f"Nationality(id={self.id}, name={self.name})"