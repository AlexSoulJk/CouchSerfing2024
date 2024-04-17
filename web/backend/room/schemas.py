from typing import Optional

from pydantic import BaseModel, ConfigDict
from datetime import datetime


class RoomBase(BaseModel):
    description: str
    price: Optional[int] = None
    location: str


class RoomUpdateParticle(BaseModel):
    description: Optional[str] = None
    price: Optional[int] = None
    location: Optional[str] = None


class RoomCreate(RoomBase):
    pass


class Room(RoomBase):
    id: int
    date_created: datetime
    model_config = ConfigDict(from_attributes=True)


class RoomGet(Room):
    date_disabled: Optional[datetime] = None
    date_delete: Optional[datetime] = None
