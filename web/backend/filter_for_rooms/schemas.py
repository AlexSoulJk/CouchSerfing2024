from typing import Optional

from pydantic import BaseModel, ConfigDict
from datetime import datetime


class BaseFilter(BaseModel):
    pass


class StartFilter(BaseFilter):
    location: str
    date_check_in: Optional[datetime] = None