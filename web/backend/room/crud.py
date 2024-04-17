from web.backend.picture.schemas import Picture, PictureCreate
from web.backend.room.schemas import RoomCreate, RoomUpdateParticle
from database.db import db
from database.models import Room
from ..rule.schemas import RuleCreate


async def create_room(room_in: RoomCreate,
                      user_id: int):
    dict_ = room_in.model_dump()
    dict_["user_id"] = user_id
    new_room = await db.create_object(model=Room, **dict_)
    return new_room


async def update_room(room_id: int,
                      room_update: RoomUpdateParticle,
                      rules_delete: list[RuleCreate],
                      rules_create_list: list[RuleCreate],
                      picture_delete_list: list[Picture],
                      picture_create_list: list[PictureCreate]):
    pass
