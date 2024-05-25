from fastapi import APIRouter, Depends
from . import crud
from .schemas import Room, RoomCreate, RoomUpdateParticle, RoomGet
from ..auth.schemas import UserRead
from ..dependencies import get_room_by_id, current_user_check_token

router = APIRouter(tags=["Rooms"])


@router.post("/{user_id}/", response_model=Room)
async def create_room(room: RoomCreate,
                      user: UserRead = Depends(current_user_check_token)):
    return await crud.create_room(room_in=room, user_id=user.id)


@router.patch("/{room_id}/{is_particle}/", response_model=Room)
async def update_particle(room_update: RoomUpdateParticle,
                          is_particle: bool,
                          room: RoomGet = Depends(get_room_by_id)):
    return await crud.update_room(room_update=room_update,
                                  particle=is_particle,
                                  room_last=room)


# Роутер для вывода комнат, которые добавил пользователь.
@router.get("/{user_id}/{is_disabled}/", response_model=list[Room])
async def get_rooms_by_user_id(is_disabled: bool,
                               user: UserRead = Depends(current_user_check_token)):
    return await crud.get_rooms(user.id, is_disabled)


# Роутер для изменения активности комнаты, которые добавил пользователь.
@router.patch("{user_id}/{room_id}/{is_disabling}")
async def update_disable_date_room_by_room_id(is_disabling: bool,
                                              room: RoomGet = Depends(get_room_by_id),
                                              user: UserRead = Depends(current_user_check_token)):
    return await crud.update_disable_date(user_id=user.id,
                                          room_last=room,
                                          is_disabling=is_disabling)


# Роутер для изменения удаление комнаты, которую добавил пользователь.
@router.delete("{user_id}/{room_id}/")
async def delete_room_by_room_id(user: UserRead = Depends(current_user_check_token),
                                 room: RoomGet = Depends(get_room_by_id)):
    return await crud.delete_room(user_id=user.id,
                                  room_last=room)
