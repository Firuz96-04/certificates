from app.core.database import Base
from typing import List
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import SmallInteger, String
from .city import City


class Country(Base):

    __tablename__ = 'countries'

    id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(40))
    cities: Mapped[List["City"]] = relationship("City", back_populates="country")

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Country(id={self.id}, name={self.name})"
