from typing import Annotated, Optional

from fastapi import Path, HTTPException, status, Depends
from sqlalchemy import select

from database.db import db
from database.models import Room
from .auth.schemas import UserRead
from .room.schemas import RoomGet
from .auth.router import fastapi_users_

from sqlalchemy.orm import class_mapper


def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in class_mapper(obj.__class__).columns}


async def get_room_by_id(room_id: Annotated[int, Path]) -> RoomGet:
    room = await db.sql_query(query=select(Room).where(Room.id == room_id))
    if room is not None:
        return RoomGet(**object_as_dict(room))

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Room with id {room_id} not found")


async def current_user_check_token(user_id: Annotated[int, Path],
                                   user=Depends(fastapi_users_.current_user(active=True))) -> UserRead:
    if user is None or user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not permitted to perform this action.",
        )
    return user


async def get_current_user_by_token(user=Depends(fastapi_users_.current_user())) -> Optional[UserRead]:
    return user


async def get_user_by_token(user=Depends(fastapi_users_.current_user(active=True))) -> Optional[UserRead]:
    return user
