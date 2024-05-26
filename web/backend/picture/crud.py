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


async def get_ids(pictures: list[PictureUpdate]):
    picture_ids = [picture.id for picture in pictures]

    res = False

    for item in await db.sql_query(query=select(RoomPicture.is_front)
            .where(RoomPicture.id.in_(picture_ids)),
                                   single=False):
        res += item

    if res:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Can't disable front object.")
    else:
        return picture_ids


async def disable_pictures_in_room_by_ids(pictures: list[PictureUpdate], room_id: int):
    picture_ids = await get_ids(pictures)
    res = await db.sql_query(query=update(RoomPicture).where(
        RoomPicture.room_id == room_id).where(
        RoomPicture.id.in_(picture_ids)).values(date_disabled=datetime.datetime.now()), is_update=True)
    if res.rowcount == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"In room {room_id} aren't found some picture to update")


async def delete_pictures_in_room_by_ids(pictures: list[PictureUpdate], room_id: int):
    picture_ids = await get_ids(pictures)
    res = await db.delete(query=delete(RoomPicture).where(
        RoomPicture.room_id == room_id).where(
        RoomPicture.id.in_(picture_ids)).where(
        RoomPicture.date_disabled == null()))
    if res.rowcount == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"In room {room_id} aren't found some picture to update")


# TODO: Подумать над использованием флага is_single
async def get_card_picture(room_id: int, is_single=True, is_all=False):
    stmt = (select(RoomPicture).where(
        RoomPicture.room_id == room_id).where(
        RoomPicture.date_disabled == null()).order_by(RoomPicture.id)
            , select(RoomPicture).where(
        RoomPicture.room_id == room_id).where(
        RoomPicture.date_disabled == null())
            .where(RoomPicture.is_front).order_by(RoomPicture.id))[is_single]

    stmt = (stmt, select(RoomPicture).where(
        RoomPicture.room_id == room_id).order_by(RoomPicture.id))[is_all]

    picture = await db.sql_query(query=stmt, single=is_single)

    if picture is not None:
        return picture

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Room with  room_id: {room_id} hasn't got any photo")
