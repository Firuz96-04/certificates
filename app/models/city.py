from app.core.database import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey, SmallInteger, String
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .country import Country
    from .district import District


class City(Base):

    __tablename__ = 'cities'

    id: Mapped[int] = mapped_column(SmallInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    country_id: Mapped[int] = mapped_column(ForeignKey("countries.id"))
    country: Mapped["Country"] = relationship("Country", back_populates="cities")
    districts: Mapped[List["District"]] = relationship("District", back_populates="city")

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"City(id={self.id}, name={self.name})"