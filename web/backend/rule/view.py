from fastapi import APIRouter, Depends
from . import crud
from ..rule.schemas import RuleCreate, RuleGet
from ..dependencies import get_room_by_id
from ..room.schemas import RoomGet

router = APIRouter(tags=["Rules"])


@router.post("/{room_id}/")
async def create_rules_in_room(rules: list[RuleCreate],
                               room: RoomGet = Depends(get_room_by_id)):
    await crud.create_rule_in_room(rules=rules, room_id=room.id)


@router.get("/{room_id}/", response_model=list[RuleGet])
async def get_rules_by_room_id(room: RoomGet = Depends(get_room_by_id)):
    return await crud.get_rules_in_room(room_id=room.id)


@router.get("not_in/{room_id}/", response_model=list[RuleGet])
async def get_rules_not_in_room_by_id(room: RoomGet = Depends(get_room_by_id)):
    return await crud.get_rules_not_in_room(room_id=room.id)


@router.get("/", response_model=list[RuleGet])
async def get_all_rules():
    return await crud.get_all_rules()


@router.delete("/{room_id}/")
async def delete_rules_in_room(rules: list[RuleCreate],
                               room: RoomGet = Depends(get_room_by_id)):
    await crud.delete_rule_in_room_by_ids(rules=rules, room_id=room.id)
