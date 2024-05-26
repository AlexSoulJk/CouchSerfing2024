from fastapi import APIRouter, Depends
from . import crud
from ..auth.schemas import UserRead, UserUpdate
from ..dependencies import get_user_by_token

router = APIRouter(tags=["Users"])


@router.patch("/", response_model=UserRead)
async def user_update(user_info: UserUpdate,
                      user: UserRead = Depends(get_user_by_token)):
    return await crud.update_user(user_info, user)


# Роутер для вывода комнат, которые добавил пользователь.
@router.get("/", response_model=UserRead)
async def get_user(user: UserRead = Depends(get_user_by_token)):
    return user
