from fastapi import APIRouter, Depends
from . import crud
from ..auth.schemas import UserRead
from web.backend.facilities.schemas import FacilityCreate, \
    FacilityGet, FacilityForChange, FacilityGetForChange
from ..dependencies import get_room_by_id, get_user_by_token
from ..room.schemas import RoomGet

router = APIRouter(tags=["Facilities"])


@router.post("create/{room_id}/")
async def create_facilities_in_room(facilities: list[FacilityCreate],
                               room: RoomGet = Depends(get_room_by_id),
                               user: UserRead = Depends(get_user_by_token)):
    await crud.create_facilities_in_room(facilities=facilities, room_id=room.id)


@router.get("/{room_id}/", response_model=list[FacilityGet])
async def get_facilities_by_room_id(room: RoomGet = Depends(get_room_by_id)):
    return await crud.get_facilities_in_room(room_id=room.id)


# Запрос для получения всех правил комнаты.
# Доступен для авторизованного пользователя в момент создания комнаты
@router.get("/", response_model=list[FacilityGet])
async def get_all_facilities():
    return await crud.get_all_facilities()



@router.delete("/{room_id}/")
async def delete_facilities_in_room(facilities: list[FacilityCreate],
                                    room: RoomGet = Depends(get_room_by_id),
                                    user: UserRead = Depends(get_user_by_token)):
    await crud.delete_facilities_in_room_by_ids(facilities=facilities, room_id=room.id)


# Изменение правил комнаты для авторизованного пользователя.
@router.patch("/")
async def update_facilities_in_room(rules: list[FacilityForChange],
                                    user: UserRead = Depends(get_user_by_token)):
    await crud.update_facilities(rules=rules)


# Получение списка выбранных правил в комнате.
# Используется в момент изменения комнаты.
@router.post("change/{room_id}/", response_model=list[FacilityGetForChange])
async def get_list_facilities_for_change_by_room_id(room: RoomGet = Depends(get_room_by_id),
                                                    user: UserRead = Depends(get_user_by_token)):
    return await crud.get_facilities_in_room_for_change(room_id=room.id)
