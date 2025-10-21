from typing import List

from pydantic import BaseModel, Field


class CountryBase(BaseModel):
    name: str = Field(max_length=30, description='Название страны')


class CountrySchema(CountryBase):
    id: int = Field(description='Код страны')


class CountryListSchema(BaseModel):
    data: List[CountrySchema]
    total: int = Field(default=0)


class CountryRead(BaseModel):
    id: int