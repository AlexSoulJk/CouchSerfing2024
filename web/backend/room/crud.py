from web.backend.picture.schemas import Picture, PictureCreate
from web.backend.room.schemas import RoomCreate
from database.db import db
from database.models import Room
from ..picture.crud import create_pictures_in_room
from ..rule.crud import create_rule_in_room
from ..rule.schemas import RuleCreate


async def create_room(room_in: RoomCreate,
                      user_id: int,
                      pictures: list[PictureCreate], rules: list[RuleCreate]):

    dict_ = room_in.model_dump()
    dict_["user_id"] = user_id

    new_room = await db.create_object(model=Room, **dict_)

    pictures_new = await create_pictures_in_room(pictures, new_room.id)
    rules_new = await create_rule_in_room(rules, new_room.id)

    return new_room



