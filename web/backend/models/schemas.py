from typing import Optional

from pydantic import BaseModel


class SUserAdd(BaseModel):
    nickname: str
    login: str
    hashed_password: str
    email: str
    telegram_tag: Optional[str] = None
    is_active: bool
    is_superuser: bool
    is_verified: bool


class SUser(SUserAdd):
    id: int
    # date_created: datetime
    # date_deleted: Optional[datetime] = None
