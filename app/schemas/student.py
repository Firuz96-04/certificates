from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime
import enum


class EducationEnum(str, enum.Enum):
    GRANT = 'grant'
    CONTRACT = 'contract'
    UNKNOWN = 'unknown'


class StudentBase(BaseModel):
    first_name: str = Field(..., max_length=30)
    last_name: str = Field(..., max_length=30)
    third_name: Optional[str] = Field(max_length=20)
    gender: bool = Field(default=True)
    born: date
    jshir: str = Field(..., max_length=14)
    passport: str = Field(..., max_length=14)
    address: Optional[str] = Field()
    education_type: EducationEnum = Field(default=EducationEnum.UNKNOWN)
    phone1: Optional[str] = Field(max_length=14)
    phone2: Optional[str] = Field(max_length=14)
    is_active: bool = Field(default=True)


class StudentCreate(StudentBase):
    nationality_id: int = Field(..., alias='nationality')
    district_id: int = Field(..., alias='district')


class StudentRead(StudentBase):
    pass
