from sqlalchemy import select, update, case, delete
from database.models import QuestionRule, QuestionOther, AnswerRule, AnswerOther, UserAnswerRule, UserAnswerOther
from database.db import db
from ..questions_and_answers.schemas import FieldsForFormGet, Question, AnswerGet, AnswerCreate, AnswerUpdate, \
    AnswerDelete, FieldsForFormGetChange, AnswerChangeGet


# classquest = lambda flag: (QuestionOther, QuestionRule)[flag]


async def get_all_reg_fields():
    res = [FieldsForFormGet(question=Question(description=item.description),
                            answers=[AnswerGet(id=answer.id, description=answer.description)
                                     for answer in await db.sql_query(select(AnswerRule)
                                                                      .where(AnswerRule.quest_id == item.id),
                                                                      single=False)])
           for item in await db.sql_query(query=select(QuestionRule),
                                          single=False)]

    res += [FieldsForFormGet(question=Question(description=item.description),
                             answers=[AnswerGet(id=answer.id, description=answer.description)
                                      for answer in await db.sql_query(select(AnswerOther)
                                                                       .where(AnswerOther.question_other_id == item.id),
                                                                       single=False)])
            for item in await db.sql_query(query=select(QuestionOther),
                                           single=False)]
    return res


async def set_user_answers(answers_id: list[AnswerCreate],
                           is_rules: bool,
                           user_id: int):
    # TODO: Возможно стоит написать проверку на наличие answer_id в базе)
    if is_rules:
        await db.create_objects([UserAnswerRule(answer_id=ans_id.answer_id,
                                                user_id=user_id) for ans_id in answers_id])
    else:
        await db.create_objects([UserAnswerOther(answer_id=ans_id,
                                                 user_id=user_id) for ans_id in answers_id])
    return True


async def update_user_answers(answers_id: list[AnswerUpdate],
                              is_rules: bool,
                              user_id: int):
    # TODO: Возможно стоит написать проверку на наличие answer_id в базе)

    if is_rules:
        whens = [(UserAnswerRule.id == answer.id_user_answer, answer.new_answer_id) for answer in answers_id]
        stmt = update(UserAnswerRule) \
            .where(UserAnswerRule.id
                   .in_([item.id_user_answer for item in answers_id])) \
            .where(UserAnswerRule.user_id == user_id) \
            .values(answer_id=case(*whens, else_=UserAnswerRule.answer_id))
    else:
        whens = [(UserAnswerOther.id == answer.id_user_answer, answer.new_answer_id) for answer in answers_id]
        stmt = update(UserAnswerOther) \
            .where(UserAnswerOther.id
                   .in_([item.id_user_answer for item in answers_id])) \
            .where(UserAnswerOther.user_id == user_id) \
            .values(answer_id=case(*whens, else_=UserAnswerOther.answer_other_id))
    await db.sql_query(stmt, is_update=True)
    return True


async def get_all_filtering_fields():
    return \
        [FieldsForFormGet(question=Question(description=item.description),
                          answers=[AnswerGet(id=answer.id, description=answer.description)
                                   for answer in await db.sql_query(select(AnswerRule)
                                                                    .where(AnswerRule.quest_id == item.id),
                                                                    single=False)])
         for item in await db.sql_query(query=select(QuestionRule),
                                        single=False)]


async def delete_user_answers(answers_id: list[AnswerDelete],
                              is_rules: bool,
                              user_id: int):
    # TODO: Проверка на валидность данных.
    if is_rules:
        stmt = delete(UserAnswerRule) \
            .where(UserAnswerRule.id
                   .in_([item.id_user_answer_id for item in answers_id])) \
            .where(UserAnswerRule.user_id == user_id)

    else:
        stmt = update(UserAnswerOther) \
            .where(UserAnswerOther.id
                   .in_([item.id_user_answer_id for item in answers_id])) \
            .where(UserAnswerOther.user_id == user_id)

    return await db.delete(stmt)


async def get_all_reg_fields_for_changing(user_id: int):
    def get_info():
        return [selected_ans.answer_id for selected_ans, _ in selected_answers], \
            dict([(quest_id, selected_ans.id)
                  for selected_ans, quest_id in selected_answers])

    selected_answers = await db.sql_query(
        query=select(UserAnswerRule, QuestionRule.id)
        .join(AnswerRule, UserAnswerRule.answer_id == AnswerRule.id)
        .join(QuestionRule, AnswerRule.quest_id == QuestionRule.id)
        .where(UserAnswerRule.user_id == user_id),
        single=False, is_scalars=False
    )

    selected_answers_id, selected_info = get_info()
    res = [FieldsForFormGetChange(question=Question(description=item.description),
                                  answers=[AnswerChangeGet(id=answer.id,
                                                           description=answer.description,
                                                           is_selected=answer.id in selected_answers_id)
                                           for answer in await db.sql_query(select(AnswerRule)
                                                                            .where(AnswerRule.quest_id == item.id),
                                                                            single=False)],
                                  id_user_answer=selected_info.get(item.id))
           for item in await db.sql_query(query=select(QuestionRule),
                                          single=False)]

    selected_answers = await db.sql_query(
        query=select(UserAnswerOther, QuestionOther.id)
        .join(AnswerOther, UserAnswerOther.answer_other_id == AnswerOther.id)
        .join(QuestionOther, AnswerOther.question_other_id == QuestionOther.id)
        .where(UserAnswerOther.user_id == user_id),
        single=False, is_scalars=False
    )

    selected_answers_id, selected_info = get_info()

    res += [FieldsForFormGetChange(question=Question(description=item.description),
                                   answers=[AnswerChangeGet(id=answer.id,
                                                            description=answer.description,
                                                            is_selected=answer.id in selected_answers_id)
                                            for answer in
                                            await db.sql_query(
                                                select(AnswerOther).where(
                                                    AnswerOther.question_other_id == item.id), single=False)],
                                   id_user_answer=selected_info.get(item.id))
            for item in await db.sql_query(query=select(QuestionOther),
                                           single=False)]

    return res
