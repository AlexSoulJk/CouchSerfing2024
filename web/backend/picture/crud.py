import datetime

from fastapi import HTTPException, status
from sqlalchemy import update, delete, select, null

from web.backend.picture.schemas import PictureCreate, PictureUpdate
from database.db import db
from database.models import RoomPicture


async def create_pictures_in_room(pictures: list[PictureCreate], room_id: int):
    dict_ = []
    for picture in pictures:
        el = picture.model_dump()
        el["room_id"] = room_id
        dict_.append(RoomPicture(**el))

    await db.create_objects(dict_)


async def disable_pictures_in_room_by_ids(pictures: list[PictureUpdate], room_id: int):
    picture_ids = [picture.id for picture in pictures]

    res = await db.sql_query(query=update(RoomPicture).where(
        RoomPicture.room_id == room_id).where(
        RoomPicture.id.in_(picture_ids)).values(date_disabled=datetime.datetime.now()), is_update=True)

    if res.rowcount == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"In room {room_id} aren't found some picture to update")


async def delete_pictures_in_room_by_ids(pictures: list[PictureUpdate], room_id: int):
    picture_ids = [picture.id for picture in pictures]

    res = await db.delete(query=delete(RoomPicture).where(
            RoomPicture.room_id == room_id).where(
            RoomPicture.id.in_(picture_ids)).where(
                RoomPicture.date_disabled == null()))
    if res.rowcount == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                      detail=f"In room {room_id} aren't found some picture to update")


async def get_card_picture(room_id: int, is_single=True):
    picture = await db.sql_query(query=select(RoomPicture).where(
        RoomPicture.room_id == room_id).where(
        RoomPicture.date_disabled == null()).order_by(RoomPicture.id), single=is_single)

    if picture is not None:
        return picture

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Room with  room_id: {room_id} hasn't got any photo")
