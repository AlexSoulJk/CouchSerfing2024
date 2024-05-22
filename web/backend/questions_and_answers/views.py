from fastapi import APIRouter, Depends
from . import crud
from ..questions_and_answers.schemas import Question, FieldsForFormGet, AnswerCreate, AnswerUpdate, AnswerDelete, \
    FieldsForFormGetChange
from ..auth.schemas import UserRead
from ..dependencies import current_user_check_token

router = APIRouter(tags=["question_and_answer"])


# Выводим список вопросов + ответов для формы регистрации
@router.post("/registration_form_fields",
             response_model=list[FieldsForFormGet])
async def get_form_fields_all():
    return await crud.get_all_reg_fields()


# Выводим список вопросов + ответов из формы регистрации с пометкой выбранного ответа
@router.post("/registration_form_fields/{user_id}",
             response_model=list[FieldsForFormGetChange])
async def get_form_fields_all_for_changing(user: UserRead = Depends(current_user_check_token)):
    return await crud.get_all_reg_fields_for_changing(user.id)

# Выводим список вопросов + ответов из формы регистрации, которые нужны для фильтра
@router.post("/filtering_form_fields",
             response_model=list[FieldsForFormGet])
async def get_filtering_fields_all():
    return await crud.get_all_filtering_fields()

# Установка(создание) ответа пользователя на вопросы из формы регистрации.
# is_with_rule - параметр, который отвечает за таблицу ответов.
# Те ответы, которые связаны с фильтром - True
@router.post("/{user_id}/{is_with_rule}")
async def set_interest(answers_list: list[AnswerCreate],
                       is_with_rule: bool,
                       user: UserRead = Depends(current_user_check_token)) -> bool:
    return await crud.set_user_answers(answers_list, is_with_rule, user.id)

# Изменение ответов пользователя на вопросы из формы регистрации.
# is_with_rule - параметр, который отвечает за таблицу ответов.
# Те ответы, которые связаны с фильтром - True.
# TODO: Подумать, над тем, какой id для update и где front может их найти нужен.
@router.post("/{user_id}/{is_with_rule}")
async def update_interest(answers_list: list[AnswerUpdate],
                          is_with_rule: bool,
                          user: UserRead = Depends(current_user_check_token)) -> bool:
    return await crud.update_user_answers(answers_list, is_with_rule, user.id)

# Удаление ответов пользователя на вопросы из формы регистрации.
# is_with_rule - параметр, который отвечает за таблицу ответов.
# Те ответы, которые связаны с фильтром - True.
@router.delete("/{user_id}/{is_with_rule}")
async def delete_interests(answers_list: list[AnswerDelete],
                           is_with_rule: bool,
                           user: UserRead = Depends(current_user_check_token)):
    return await crud.delete_user_answers(answers_list, is_with_rule, user.id)
