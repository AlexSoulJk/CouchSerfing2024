from pydantic import BaseModel
from typing import List, Optional


class Question(BaseModel):
    description: str


class QuestionGet(Question):
    id: int


class Answer(BaseModel):
    description: str


class AnswerGet(Answer):
    id: int


class AnswerChangeGet(AnswerGet):
    is_selected: bool


class FieldsForFormGet(BaseModel):
    question: Question
    answers: List[AnswerGet]


class FieldsForFormGetChange(BaseModel):
    id_user_answer: Optional[int]
    question: Question
    answers: List[AnswerChangeGet]



class AnswerCreate(BaseModel):
    answer_id: int


class AnswerDelete(BaseModel):
    answer_id: int


class AnswerUpdate(BaseModel):
    id_user_answer_id: int
    new_answer_id: int
