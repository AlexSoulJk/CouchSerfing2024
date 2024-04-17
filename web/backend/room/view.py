from fastapi import APIRouter
from . import crud
from .schemas import Room, RoomCreate, RoomUpdateParticle
from ..rule.schemas import RuleCreate
from ..picture.schemas import PictureCreate, Picture

router = APIRouter(tags=["Rooms"])


@router.post("/{user_id}/", response_model=Room)
async def create_room(user_id: int,
                      room: RoomCreate):
    return await crud.create_room(room_in=room, user_id=user_id)


@router.patch("/{room_id}/", response_model=Room)
async def update_particle(room_id: int,
                          room_update: RoomUpdateParticle,
                          rules_delete: list[RuleCreate],
                          rules_create_list: list[RuleCreate],
                          picture_delete_list: list[Picture],
                          picture_create_list: list[PictureCreate]):
    pass
