from typing import Annotated

from fastapi import Path, HTTPException, status
from sqlalchemy import select

from database.db import db
from database.models import Room
from .room.schemas import RoomGet


async def get_room_by_id(room_id: Annotated[int, Path]) -> RoomGet:
    room = await db.sql_query(query=select(Room).where(Room.id == room_id))
    if room is not None:
        return room

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Room with id {room_id} not found")
