from typing import Optional

from pydantic import BaseModel, ConfigDict
from datetime import datetime


class BaseFilter(BaseModel):
    pass


class StartFilter(BaseFilter):
    location: str
    date_check_in: Optional[datetime] = None


class MainFilter(StartFilter):
    pass


class RoomSchema(BaseModel):
    id: int
    location: str
    price: int
    description: Optional[str] = None
    date_created: Optional[datetime] = None
    date_disabled: Optional[datetime] = None
    date_deleted: Optional[datetime] = None

    class Config:
        from_attributes = True


class Picture(BaseModel):
    url_picture: Optional[str]


class CardSchema(BaseModel):
    room: RoomSchema
    picture: Picture

    class Config:
        from_attributes = True
