from sqlalchemy import Integer, String, Boolean, DateTime, Date, Text, ForeignKey, func, Enum, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, date
from app.core.database import Base



class Student(Base):

    __tablename__ = 'students'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(30))
    second_name: Mapped[str] = mapped_column(String(30))
    third_name: Mapped[str] = mapped_column(String(30), nullable=True)
    gender: Mapped[bool] = mapped_column(Boolean, default=True)
    born: Mapped[date] = mapped_column(Date, nullable=True)
    jshir: Mapped[str] = mapped_column(String(14), nullable=True)
    passport: Mapped[str] = mapped_column(String(10), nullable=True)
    address: Mapped[str] = mapped_column(Text, nullable=True)
    education_type: Mapped[str] = mapped_column(String(10))
    phone1: Mapped[str] = mapped_column(String(14), nullable=True)
    phone2: Mapped[str] = mapped_column(String(14), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    nationality_id: Mapped[int] = mapped_column(ForeignKey("nationalities.id"),)
    nationality: Mapped["Nationality"] = relationship("Nationality", back_populates="students")
    district_id: Mapped[int] = mapped_column(ForeignKey("districts.id"),)
    district: Mapped["District"] = relationship("District", back_populates="students")
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    def __str__(self):
        return f"{self.first_name} {self.second_name}"

