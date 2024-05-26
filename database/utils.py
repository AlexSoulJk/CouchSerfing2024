import json

from sqlalchemy import select

from database.models import QuestionRoomRule, Rule, QuestionRule, AnswerRule, Facility, QuestionOther, AnswerOther


async def check_is_empty_table(model, db):
    return len(await db.sql_query(query=select(model), single=False)) == 0


async def upload_question(filename, db):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if not await check_is_empty_table(QuestionRoomRule, db):
        return

    for item in data:

        question_room_rule = item.get("QuestionRoomRule")
        new_question_room_rule = await db.create_object(model=QuestionRoomRule, **question_room_rule)

        question_rule = item.get("QuestionRule")
        new_question_rule = await db.create_object(model=QuestionRule, **question_rule)

        rules = item.get("Rules")
        answers = item.get("AnswerRules")

        if rules is None:
            raise "Ban rules"
        if answers is None:
            raise "Ban answer"

        # TODO: Проверка на соответствие правил и ответов(чисто по кол-ву).

        for i, rule in enumerate(rules):
            new_rule = rule.copy()
            new_rule["quest_id"] = new_question_room_rule.id
            new_object = await db.create_object(model=Rule, **new_rule)
            new_answer = answers[i].copy()
            new_answer["quest_id"] = new_question_rule.id
            new_answer["rule_id"] = new_object.id
            await db.create_object(model=AnswerRule, **new_answer)


async def upload_facilities(filename, db):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if not await check_is_empty_table(Facility, db):
        return

    for item in data:
        await db.create_object(model=Facility, **item)


async def upload_question_other(filename, db):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if not await check_is_empty_table(QuestionOther, db):
        return

    for item in data:
        question_other = item.get("QuestionOther")
        new_question = await db.create_object(model=QuestionOther, **question_other)
        answers = item.get("AnswersOthers")

        for ans in answers:
            tmp = ans.copy()
            tmp["question_other_id"] = new_question.id
            await db.create_object(model=AnswerOther, **tmp)
