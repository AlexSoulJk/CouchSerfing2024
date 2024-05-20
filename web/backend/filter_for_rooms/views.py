from fastapi import APIRouter, Depends

from .schemas import StartFilter, MainFilter
from ..auth.schemas import UserRead
from ..dependencies import get_room_by_id, \
    current_user_check_token, get_current_user_by_token
import crud

router = APIRouter(tags=["Rooms"])


# Роутер для получения комнат по стартовому фильтру.
@router.get("/start")
async def get_start_list(start_filter: StartFilter,
                         user=Depends(get_current_user_by_token)):
    return await crud.get_start_list_for_user(user, start_filter)


@router.get("/main_page")
async def get_start_list(start_filter: MainFilter,
                         user=Depends(get_current_user_by_token)):
    return await crud.get_main_list_for_user(user, start_filter)
