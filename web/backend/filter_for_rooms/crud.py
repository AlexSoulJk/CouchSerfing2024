from typing import Optional

from sqlalchemy import select, not_, null

from database.db import db
from database.models import UserAnswerRule, Room, RoomRule, RoomPicture, Rule, AnswerRule
from web.backend.auth.schemas import UserRead
from web.backend.filter_for_rooms.schemas import StartFilter, MainFilter, CardSchema, RoomSchema, Picture


def applied_rules(user: Optional[UserRead]):
    return (select(Rule.id)
            .join(AnswerRule, AnswerRule.rule_id == Rule.id)
            .join(UserAnswerRule, UserAnswerRule.answer_id == AnswerRule.id)
            .where(UserAnswerRule.user_id == user.id))


# TODO: Протестить stm1 & stm2
# Для stm1 необходимо добавить в базу:
# 2-ух пользователей, с одного добавляешь комнаты, с другого их ищешь.(через swagger)
# Для одного пользователя добавить ответы на вопросы(Пока что руками в бд)
# Добавить картинку и правила для комнаты.
# Для stm2 необходимо:
# Просто проверить работоспособность на неавторизованном пользователе
async def get_start_list_for_user(user: Optional[UserRead],
                                  start_filter: StartFilter):
    subquery = select(RoomPicture.url_picture).where(
        Room.id == RoomPicture.room_id).order_by(
        RoomPicture.date_created).where(RoomPicture.is_front).scalar_subquery()
    print(user)
    if user is not None:
        # Запрос для комнат, которые не принадлежат пользователю и подходящих идентификаторам правил пользователя.
        stmt = applied_rules(user)
        # stmt = select(UserAnswerRule.answer_id).where(UserAnswerRule.user_id == user.id)
        print("stmt = ", str(stmt))
        answers_id = await db.sql_query(stmt, single=False)
        print(answers_id)
        if len(answers_id) != 0:
            # Пользователь авторизован + есть анкета интересов. stm1
            stmt = (
                select(Room, subquery.label('picture_url'))
                .join(RoomRule, Room.id == RoomRule.room_id)
                .where(Room.user_id != user.id)
                .where(Room.location == start_filter.location)
                .where(Room.date_disabled == null())
                .where(Room.date_deleted == null())
                .where(RoomRule.rule_id.in_(
                    answers_id))
                .group_by(Room.id)
                .order_by(Room.price)
            )
            print(str(stmt))
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
        # Если пользователь не авторизован, возвращаем все активные комнаты. stm2
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
                                 main_filter: MainFilter):
    subquery = select(RoomPicture.url_picture).where(
        Room.id == RoomPicture.room_id).order_by(
        RoomPicture.date_created).where(RoomPicture.is_front).scalar_subquery()
    print(user)
    if user is not None:
        print("main filter")
        stmt = applied_rules(user)
        # stmt = select(UserAnswerRule.answer_id).where(UserAnswerRule.user_id == user.id)
        print("stmt = ", str(stmt))
        answers_id = await db.sql_query(stmt, single=False)
        print(answers_id)
        if len(answers_id) != 0:
            stmt = (
                select(Room, subquery.label('picture_url'))
                .join(RoomRule, Room.id == RoomRule.room_id)
                .where(Room.user_id != user.id)
                .where(Room.location == main_filter.location)
                .where(Room.price >= main_filter.min_price)
                .where(Room.price <= main_filter.max_price)
                .where(Room.capacity >= main_filter.guest_count)
                .where(Room.floor_number >= main_filter.min_floor)
                .where(Room.floor_number <= main_filter.max_floor)
                .where(Room.date_disabled == null())
                .where(Room.date_deleted == null())
                .where(RoomRule.rule_id.in_(
                    answers_id))
                .group_by(Room.id)
                .order_by(Room.price)
            )
            print(str(stmt))
    else:
        stmt = (select(Room, subquery.label('picture_url'))
                .where(Room.location == main_filter.location)
                .where(Room.date_disabled == null())
                .where(Room.date_deleted == null())
                .order_by(Room.price))
    rooms_and_pictures = await db.sql_query(stmt, single=False, is_scalars=False)
    cards = [CardSchema(room=RoomSchema.from_orm(room), picture=Picture(url_picture=pic)) for room, pic
             in rooms_and_pictures]
    return cards
    # Совместить основным фильтр с данными, которые получились по
    # информации из анкеты пользователя учесть, что теперь приоритет
    # выделяется на пользовательские отметки.

    pass
