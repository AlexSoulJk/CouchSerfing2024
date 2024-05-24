import sqlalchemy
from sqlalchemy import delete, select, case, update

from database.db import db
from database.models import RoomRule, Room, Rule, QuestionRoomRule
from web.backend.rule.schemas import RuleCreate, CardRuleGet, Question, RuleGet, CardRuleGetForChange, RuleGetForChange, \
    RuleForChange
from fastapi import HTTPException, status


async def create_rule_in_room(rules: list[RuleCreate], room_id: int):
    dict_ = []
    for rule in rules:
        el = rule.model_dump()
        el["room_id"] = room_id
        dict_.append(RoomRule(**el))
    try:
        await db.create_objects(dict_)
    except sqlalchemy.exc.IntegrityError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"In room with id {room_id} some rule are not founded")


async def delete_rule_in_room_by_ids(rules: list[RuleCreate], room_id: int) -> None:
    rule_ids = [rule.rule_id for rule in rules]
    res = await db.delete(query=delete(RoomRule).where(
        RoomRule.room_id == room_id).where(RoomRule.rule_id.in_(rule_ids)))

    if res.rowcount == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"In room with id {room_id} some rule are not founded")


async def get_rules_in_room(room_id: int):
    return await db.sql_query(query=select(Rule).join_from(
        RoomRule, Rule).where(
        RoomRule.room_id == room_id), single=False)


async def get_all_rules():
    res = [CardRuleGet(question=Question(description=item.description),
                       answers=[RuleGet(id=answer.id, description=answer.description)
                                for answer in await db.sql_query(select(Rule)
                                                                 .where(Rule.quest_id == item.id),
                                                                 single=False)],
                       is_with_rule=True)
           for item in await db.sql_query(query=select(QuestionRoomRule),
                                          single=False)]
    return res


async def get_rules_not_in_room(room_id: int):
    return await db.sql_query(query=select(Rule).join(
        RoomRule, Rule.id != RoomRule.rule_id).where(RoomRule.room_id == room_id))


async def get_rules_in_room_for_change(room_id: int):
    def get_info():
        return [selected_ans.answer_id for selected_ans, _ in selected_answers], \
            dict([(quest_id, selected_ans.id)
                  for selected_ans, quest_id in selected_answers])

    selected_answers = await db.sql_query(
        query=select(RoomRule, QuestionRoomRule.id)
        .join(Rule, RoomRule.rule_id == Rule.id)
        .join(QuestionRoomRule, Rule.quest_id == QuestionRoomRule.id)
        .where(RoomRule.room_id == room_id),
        single=False, is_scalars=False
    )

    selected_answers_id, selected_info = get_info()
    res = [CardRuleGetForChange(question=Question(description=item.description),
                                answers=[RuleGetForChange(id=answer.id,
                                                          description=answer.description,
                                                          is_selected=answer.id in selected_answers_id)
                                         for answer in await db.sql_query(select(Rule)
                                                                          .where(Rule.quest_id == item.id),
                                                                          single=False)],
                                id_user_answer=selected_info.get(item.id))
           for item in await db.sql_query(query=select(QuestionRoomRule),
                                          single=False)]
    return res


def update_rules(rules: list[RuleForChange]):
    whens = [(RoomRule.id == rule.id_user_answer, rule.id_rule) for rule in rules]

    stmt = update(RoomRule) \
        .where(RoomRule.id
               .in_([item.id_user_answer for item in rules])) \
        .values(rule_id=case(*whens, else_=RoomRule.rule_id))

    await db.sql_query(stmt, is_update=True)