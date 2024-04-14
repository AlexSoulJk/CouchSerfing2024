from web.backend.picture.schemas import PictureCreate
from database.db import db
from database.models import RoomPicture


async def create_pictures_in_room(pictures: list[PictureCreate], room_id: int):

    dict_ = []
    for picture in pictures:
        el = picture.model_dump()
        el["room_id"] = room_id
        dict_.append(RoomPicture(**el))

    await db.create_objects(dict_)
