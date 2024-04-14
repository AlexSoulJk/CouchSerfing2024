from fastapi import APIRouter
from . import crud
from .schemas import Room, RoomCreate
from ..rule.schemas import RuleCreate
from ..picture.schemas import PictureCreate

router = APIRouter(tags=["Rooms"])


@router.post("/{user_id}/", response_model=Room)
async def create_room(user_id: int,
                      room: RoomCreate,
                      rules: list[RuleCreate],
                      pictures: list[PictureCreate]):
    return await crud.create_room(room_in=room, user_id=user_id,
                                  pictures=pictures, rules=rules)


