from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from typing import List


class District(Base):
    __tablename__ = 'districts'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"))
    city: Mapped["City"] = relationship("City", back_populates="districts")
    students: Mapped[List["Student"]] = relationship("Student", back_populates="district")

    def __str__(self):
        return self.name
