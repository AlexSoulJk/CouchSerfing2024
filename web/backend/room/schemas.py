from typing import Optional

from pydantic import BaseModel, ConfigDict
from datetime import datetime


class RoomBase(BaseModel):
    description: str
    price: Optional[int] = None
    location: str


class RoomCreate(RoomBase):
    pass


class Room(RoomBase):
    id: int
    date_created: datetime
    model_config = ConfigDict(from_attributes=True)

