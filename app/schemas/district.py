from pydantic import BaseModel, Field


class DistrictBase(BaseModel):
    name: str = Field(max_length=40, description='district name')
    city_id: int = Field(description='district city id')


class DistrictCreate(DistrictBase):
    pass


class UpdateDistrictBase(DistrictBase):
    name: str | None = Field(default=None, description='district name')
    city_id: int | None = Field(default=None, description='district city id')


class DistrictRead(DistrictBase):
    id: int = Field(description='district id')

