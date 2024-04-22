from fastapi import APIRouter, Depends
from . import crud
from .schemas import Room, RoomCreate, RoomUpdateParticle, RoomGet
from ..dependencies import get_room_by_id

router = APIRouter(tags=["Rooms"])


# TODO: Добавить зависимость от авторизованности
#  пользователя + проверка на существование
@router.post("/{user_id}/", response_model=Room)
async def create_room(user_id: int,
                      room: RoomCreate):
    return await crud.create_room(room_in=room, user_id=user_id)


@router.patch("/{room_id}/{is_particle}/", response_model=Room)
async def update_particle(room_update: RoomUpdateParticle,
                          is_particle: bool,
                          room: RoomGet = Depends(get_room_by_id)):
    return await crud.update_room(room_update=room_update,
                                  particle=is_particle,
                                  room_last=room)


@router.get("/{user_id}/{is_disabled}/", response_model=list[Room])
async def get_rooms_by_user_id(user_id: int, is_disabled: bool):
    return await crud.get_rooms(user_id, is_disabled)


@router.patch("{user_id}/{room_id}/{is_disabling}")
async def update_disable_date_room_by_room_id(user_id: int,
                                              is_disabling: bool,
                                              room: RoomGet = Depends(get_room_by_id)):
    return await crud.update_disable_date(user_id=user_id,
                                          room_last=room,
                                          is_disabling=is_disabling)


@router.delete("{user_id}/{room_id}/")
async def delete_room_by_room_id(user_id: int,
                                 room: RoomGet = Depends(get_room_by_id)):
    pass