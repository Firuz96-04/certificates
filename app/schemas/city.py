from pydantic import BaseModel, Field
from typing import Optional
from .country import CountryRead


class CityBase(BaseModel):
    name: str = Field(description='City name')


class CityCreate(CityBase):
    country_id: int = Field(description='Country ID')


class CityUpdate(BaseModel):
    name: Optional[str] = Field(default=None)
    country_id: Optional[int] = Field(default=None)


class CityRead(CityBase):
    id: int
    # country_id: Optional[int] = Field(default=None)
    country: CountryRead

    # class Config:
    #     from_attributes = True
