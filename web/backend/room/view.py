from fastapi import APIRouter, Depends
from . import crud
from .schemas import RoomS, RoomCreate, RoomUpdateParticle, RoomGet
from ..auth.schemas import UserRead
from ..dependencies import get_user_by_token, is_room_owner, get_room_by_id

router = APIRouter(tags=["Rooms"])


@router.post("/", response_model=RoomS)
async def create_room(room: RoomCreate,
                      user: UserRead = Depends(get_user_by_token)):
    return await crud.create_room(room_in=room, user_id=user.id)


@router.patch("/{room_id}/{is_particle}/", response_model=RoomS)
async def update_particle(room_update: RoomUpdateParticle,
                          is_particle: bool,
                          room: RoomGet = Depends(is_room_owner)):
    return await crud.update_room(room_update=room_update,
                                  particle=is_particle,
                                  room_last=room)


# Роутер для вывода комнат, которые добавил пользователь.
@router.get("/{is_disabled}/", response_model=list[RoomS])
async def get_rooms_by_user_id(is_disabled: bool,
                               user: UserRead = Depends(get_user_by_token)):
    return await crud.get_rooms(user.id, is_disabled)


@router.get("/{room_id}/room", response_model=RoomGet)
async def get_rooms_by_room_id(room: RoomGet = Depends(get_room_by_id)):
    return room


# Роутер для изменения активности комнаты, которые добавил пользователь.
@router.patch("/{room_id}/{is_disabling}")
async def update_disable_date_room_by_room_id(is_disabling: bool,
                                              room: RoomGet = Depends(is_room_owner)):
    return await crud.update_disable_date(room_last=room,
                                          is_disabling=is_disabling)


# Роутер для изменения удаление комнаты, которую добавил пользователь.
@router.delete("/{room_id}/")
async def delete_room_by_room_id(room: RoomGet = Depends(is_room_owner)):
    return await crud.delete_room(room_last=room)
