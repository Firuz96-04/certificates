from pydantic import BaseModel, Field
from typing import List


class Food(BaseModel):
    price: float
    name: str = Field(description='name dish')
    ingredients: List[str] | None


class Restaurant(BaseModel):
    name: str = Field(max_length=60, description='name restaurant')
    location: str
    foods: List[Food]


