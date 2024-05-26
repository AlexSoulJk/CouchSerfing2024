from sqlalchemy import update, select, null

from web.backend.room.schemas import RoomCreate, RoomUpdateParticle, RoomGet
from database.db import db
from database.models import Room
import datetime
from ..dependencies import object_as_dict


async def create_room(room_in: RoomCreate,
                      user_id: int):
    dict_ = room_in.model_dump()
    dict_["user_id"] = user_id
    new_room = await db.create_object(model=Room, **dict_)
    return new_room


async def update_room(room_update: RoomUpdateParticle,
                      room_last: RoomGet,
                      particle: bool):
    for name, item in room_update.model_dump(exclude_none=particle).items():
        setattr(room_last, name, item)

    it = room_last.model_dump()

    await db.sql_query(query=update(Room).where(Room.id == room_last.id).values(
        **room_update.model_dump(exclude_none=particle)), is_update=True)

    return it


async def get_rooms(user_id: int, is_disabled: bool):
    res = await db.sql_query(query=
                             select(Room)
                             .where(Room.user_id == user_id)
                             .where(
                                 (Room.date_disabled == null(),
                                  Room.date_disabled != null())[is_disabled])
                             .where(Room.date_deleted == null()),
                             single=False)
    return [RoomGet(**object_as_dict(it)) for it in res]


async def update_disable_date(room_last: RoomGet,
                              is_disabling: bool):
    room_last.date_disabled = (None, datetime.datetime.now())[is_disabling]
    it = room_last.model_dump().copy()
    room_id = it.pop("id")
    await db.sql_query(query=update(Room).where(Room.id == room_id)
                       .where(Room.date_deleted == null()).values(**it),
                       is_update=True)
    return RoomGet(**room_last.model_dump())


async def delete_room(room_last: RoomGet):
    room_last.date_deleted = datetime.datetime.now()
    it = room_last.model_dump().copy()
    room_id = it.pop("id")
    await db.sql_query(query=update(Room).where(Room.id == room_id).values(**it),
                       is_update=True)
    return RoomGet(**room_last.model_dump())
