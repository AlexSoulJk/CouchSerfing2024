from database.db import db
from database.models import RoomRule
from web.backend.rule.schemas import RuleCreate


async def create_rule_in_room(rules: list[RuleCreate], room_id: int):

    dict_ = []
    for rule in rules:
        el = rule.model_dump()
        el["room_id"] = room_id
        dict_.append(RoomRule(**el))

    await db.create_objects(dict_)