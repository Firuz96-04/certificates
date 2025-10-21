from http.client import HTTPException
from pydantic import BaseModel, Field, field_validator, model_validator


class BUser(BaseModel):
    id: int
    name: str = Field(default='')
    last_name: str = Field(default='')
    age: int
    gender: bool

    # @field_validator('age')
    # def check_age(cls, value):
    #     if value < 18:
    #         raise HTTPException("Age more than 18")
    #     print(value)
    #     return value

    @model_validator(mode='wrap')
    @classmethod
    def check_person(cls, values, handler):
        result = handler(values)
        # print(result, 'handler')
        return result
