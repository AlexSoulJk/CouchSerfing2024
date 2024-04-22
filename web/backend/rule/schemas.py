from pydantic import BaseModel, ConfigDict


class Rule(BaseModel):
    description: str


class RuleCreate(BaseModel):
    rule_id: int


class RuleGet(Rule):
    id: int
    url_pic: str
    model_config = ConfigDict(from_attributes=True)
