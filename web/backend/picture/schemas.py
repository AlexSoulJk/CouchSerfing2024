from pydantic import BaseModel, ConfigDict
from datetime import datetime


class PictureBase(BaseModel):
    url_picture: str


class PictureCreate(PictureBase):
    pass


class Picture(PictureBase):
    id: int
    room_id: int
    date_created: datetime
    model_config = ConfigDict(from_attributes=True)
