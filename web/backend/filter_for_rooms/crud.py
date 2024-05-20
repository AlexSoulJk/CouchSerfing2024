from typing import Optional

from sqlalchemy import select, not_, null

from database.db import db
from database.models import UserAnswerRule, Room, RoomRule, RoomPicture
from web.backend.auth.schemas import UserRead
from web.backend.filter_for_rooms.schemas import StartFilter, MainFilter, CardSchema, RoomSchema, Picture


async def get_start_list_for_user(user: Optional[UserRead],
                                  start_filter: StartFilter):
    subquery = select(RoomPicture.url_picture).where(
        Room.id == RoomPicture.room_id).order_by(
        RoomPicture.date_created).where(RoomPicture.is_front).scalar_subquery()

    if user is not None:
        # Запрос для комнат, которые не принадлежат пользователю и подходящих идентификаторам правил пользователя.
        stmt = select(UserAnswerRule.answer_id).where(UserAnswerRule.user_id == user.id)
        answers_id = await db.sql_query(stmt, single=False)
        if len(answers_id) != 0:
            stmt = (
                select(Room, subquery.label('picture_url'))
                .join(RoomRule, Room.id == RoomRule.room_id)
                .where(Room.user_id != user.id)
                .where(Room.location == start_filter.location)
                .where(Room.date_disabled == null())
                .where(Room.date_deleted == null())
                .where(RoomRule.rule_id.in_(
                    answers_id))
                .order_by(Room.price)
            )
        else:
            stmt = (
                select(Room, subquery.label('picture_url'))
                .where(Room.user_id != user.id)
                .where(Room.location == start_filter.location)
                .where(Room.date_disabled == null())
                .where(Room.date_deleted == null())
                .order_by(Room.price)
            )
    else:
        # Если пользователь не авторизован, возвращаем все активные комнаты.
        stmt = (select(Room, subquery.label('picture_url'))
                .where(Room.location == start_filter.location)
                .where(Room.date_disabled == null())
                .where(Room.date_deleted == null())
                .order_by(Room.price))
    rooms_and_pictures = await db.sql_query(stmt, single=False, is_scalars=False)
    cards = [CardSchema(room=RoomSchema.from_orm(room), picture=Picture(url_picture=pic)) for room, pic
             in rooms_and_pictures]
    return cards


async def get_main_list_for_user(user: Optional[UserRead],
                                 start_filter: MainFilter):
    if user is not None:
        # Написать запрос для сравнения по
        # правилам, которые установлены в комнате.
        # Написать запрос для фильтрации по other answers

        pass

    # Совместить основным фильтр с данными, которые получились по
    # информации из анкеты пользователя учесть, что теперь приоритет
    # выделяется на пользовательские отметки.

    pass
