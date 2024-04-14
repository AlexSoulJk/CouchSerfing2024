from pydantic import BaseModel


class Rule(BaseModel):
    description: str


class RuleCreate(BaseModel):
    id: int