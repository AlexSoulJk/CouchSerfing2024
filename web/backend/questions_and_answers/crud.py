from sqlalchemy import select
from database.models import QuestionRule, QuestionOther, AnswerRule, AnswerOther
from database.db import db
from ..questions_and_answers.schemas import FieldsForFormGet, Question, AnswerGet, AnswerCreate, AnswerUpdate, \
    AnswerDelete


async def create_fields(result):
    return [FieldsForFormGet(question=Question(description=row[0]),
                             answers=[AnswerGet(id=answer.id, description=answer.description) for answer in row[1]])
            for row in result]


async def get_all_reg_fields():
    result_rules = await db.sql_query(
        query=select(QuestionRule.description, AnswerRule)
        .join(AnswerRule, QuestionRule.id == AnswerRule.quest_id),
        single=False, is_scalars=False)

    result_others = await db.sql_query(
        query=select(QuestionOther.description, AnswerOther)
        .join(AnswerOther, QuestionOther.id == AnswerOther.question_other_id),
        single=False, is_scalars=False)

    return await create_fields(result_rules) + await create_fields(result_others)


async def set_user_answers(answers_id: list[AnswerCreate],
                           is_rules: bool,
                           user_id: int):
    return True


async def update_user_answers(answers_id: list[AnswerUpdate],
                              is_rules: bool,
                              user_id: int):
    return True


async def get_all_filtering_fields():
    pass


def delete_user_answers(answers_id: list[AnswerDelete],
                        is_rules: bool,
                        user_id: int):
    return None


def get_all_reg_fields_for_changing(user_id: int):
    return None