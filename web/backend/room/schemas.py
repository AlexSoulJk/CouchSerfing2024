from typing import Optional

from pydantic import BaseModel, ConfigDict
from datetime import datetime, time


class RoomBase(BaseModel):
    description: str
    price: Optional[int] = None
    location: str

    name: str
    capacity: int
    floor_number: int
    transport_info: str
    time_check_in: time
    time_check_out: time
    model_config = ConfigDict(from_attributes=True)


class RoomUpdateParticle(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None
    location: Optional[str] = None
    capacity: Optional[int] = None
    floor_number: Optional[int] = None
    transport_info: Optional[str] = None
    time_check_in: Optional[time] = None
    time_check_out: Optional[time] = None


class RoomCreate(RoomBase):
    pass


class RoomS(RoomBase):
    id: int
    date_created: datetime


class RoomGet(RoomS):
    date_disabled: Optional[datetime] = None
    date_deleted: Optional[datetime] = None


