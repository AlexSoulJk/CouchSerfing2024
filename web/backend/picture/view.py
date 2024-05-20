from fastapi import APIRouter, Depends
from . import crud
from ..dependencies import get_room_by_id
from ..picture.schemas import PictureCreate, Picture, PictureUpdate
from ..room.schemas import RoomGet
from fastapi import Path, HTTPException, status

router = APIRouter(tags=["Pictures"])

# TODO: Добавить зависимость от авторизации пользователя.
# TODO: Добавить нормальные исключения

@router.post("/{room_id}/")
async def create_pictures_in_room(pictures: list[PictureCreate],
                                  room: RoomGet = Depends(get_room_by_id)):
    await crud.create_pictures_in_room(pictures=pictures, room_id=room.id)


@router.get("/{room_id}/is_card/", response_model=Picture)
async def get_picture_card_by_room_id(room: RoomGet = Depends(get_room_by_id)):
    return await crud.get_card_picture(room_id=room.id)


@router.get("/{room_id}/", response_model=list[Picture])
async def get_enable_pictures_in_room(room: RoomGet = Depends(get_room_by_id)):
    return await crud.get_card_picture(room.id, False)


@router.patch("/{room_id}/")
async def disable_pictures_in_room(pictures: list[PictureUpdate],
                                   room: RoomGet = Depends(get_room_by_id)):
    await crud.disable_pictures_in_room_by_ids(pictures=pictures, room_id=room.id)


@router.delete("/{room_id}/")
async def delete_pictures_in_room(pictures: list[PictureUpdate],
                                  room: RoomGet = Depends(get_room_by_id)):
    await crud.delete_pictures_in_room_by_ids(pictures=pictures, room_id=room.id)




