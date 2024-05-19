from typing import Optional

from pydantic import BaseModel


class SUserAdd(BaseModel):
    nickname: str
    login: str
    password: str
    email: str
    telegram_tag: Optional[str] = None


class SUser(SUserAdd):
    id: int
    # date_created: datetime
    # date_deleted: Optional[datetime] = None
