from typing import List, Optional

from pydantic import BaseModel, ConfigDict


class Rule(BaseModel):
    description: str


class RuleCreate(BaseModel):
    rule_id: int


class RuleGet(Rule):
    id: int
    url_pic: str
    model_config = ConfigDict(from_attributes=True)


class RuleGetForChange(RuleGet):
    is_selected: bool


class Question(BaseModel):
    description: str


class CardRuleGet(BaseModel):
    question: Question
    rules: List[RuleGet]


class CardRuleGetForChange(BaseModel):
    id_user_answer: Optional[int]
    question: Question
    rules: List[RuleGetForChange]


class RuleForChange(BaseModel):
    id_user_answer: int
    id_rule: int
