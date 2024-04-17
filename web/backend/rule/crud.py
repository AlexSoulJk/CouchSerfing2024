import sqlalchemy
from sqlalchemy import delete, select

from database.db import db
from database.models import RoomRule, Room, Rule
from web.backend.rule.schemas import RuleCreate
from fastapi import HTTPException, status


async def create_rule_in_room(rules: list[RuleCreate], room_id: int):
    dict_ = []
    for rule in rules:
        el = rule.model_dump()
        el["room_id"] = room_id
        dict_.append(RoomRule(**el))
    try:
        await db.create_objects(dict_)
    except sqlalchemy.exc.IntegrityError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"In room with id {room_id} some rule are not founded")


async def delete_rule_in_room_by_ids(rules: list[RuleCreate], room_id: int) -> None:
    rule_ids = [rule.rule_id for rule in rules]
    res = await db.delete(query=delete(RoomRule).where(
        RoomRule.room_id == room_id).where(RoomRule.rule_id.in_(rule_ids)))

    if res.rowcount == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"In room with id {room_id} some rule are not founded")


async def get_rules_in_room(room_id: int):
    return await db.sql_query(query=select(Rule).join_from(
        RoomRule, Rule).where(
        RoomRule.room_id == room_id), single=False)


async def get_all_rules():
    return await db.sql_query(query=select(Rule))
