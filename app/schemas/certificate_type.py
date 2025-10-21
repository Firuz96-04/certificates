from pydantic import BaseModel, Field
from typing import Optional


class CertificateTypeBase(BaseModel):
    name: str
    title: str
    hours: int = Field(description='часы преповодания')
    description: str


class CertificateTypeCreate(CertificateTypeBase):
    pass


class CertificateTypeUpdate(BaseModel):
    name: Optional[str] = Field(default=None,)
    title: Optional[str] = Field(default=None)
    hours: Optional[int] = Field(default=None)
    description: Optional[str] = Field(default=None)


class CertificateTypeRead(CertificateTypeBase):
    id: int
