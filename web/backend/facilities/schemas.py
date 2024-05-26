from typing import List, Optional

from pydantic import BaseModel, ConfigDict


class Facility(BaseModel):
    description: str


class FacilityCreate(BaseModel):
    facility_id: int


class FacilityGet(Facility):
    id: int
    model_config = ConfigDict(from_attributes=True)


class FacilityGetForChange(FacilityGet):
    is_selected: bool
    id_user_answer: Optional[int]


class FacilityForChange(BaseModel):
    id_user_answer: int
    facility_id: int
