from sqlalchemy import update, select, null

from web.backend.room.schemas import RoomCreate, RoomUpdateParticle, RoomGet
from database.db import db
from database.models import Room
import datetime


async def create_room(room_in: RoomCreate,
                      user_id: int):
    dict_ = room_in.model_dump()
    dict_["user_id"] = user_id
    new_room = await db.create_object(model=Room, **dict_)
    return new_room


async def update_room(room_update: RoomUpdateParticle,
                      room_last: RoomGet,
                      particle: bool):
    for name, item in room_update.model_dump(exclude_unset=particle):
        setattr(room_last, name, item)

    return await db.sql_query(query=update(Room).value(
        **room_last.model_dump()), is_update=True)


async def get_rooms(user_id: int, is_disabled: bool):
    return await db.sql_query(query=select(Room).where(
        Room.user_id == user_id).where(
        (Room.date_disabled != null(),
         Room.date_disabled == null())[is_disabled]),
        single=False)


async def update_disable_date(user_id: int,
                              room_last: RoomGet,
                              is_disabling: bool):
    room_last.date_disabled = (null(), datetime.datetime.now())[is_disabling]
    return await db.sql_query(query=update(Room).values(**room_last.model_dump()).where(Room.user_id == user_id),
                              is_update=True)


async def delete_room(user_id: int, room_last: RoomGet):
    room_last.date_delete = datetime.datetime.now()
    return await db.sql_query(query=update(Room).values(**room_last.model_dump()).where(Room.user_id == user_id),
                              is_update=True)
