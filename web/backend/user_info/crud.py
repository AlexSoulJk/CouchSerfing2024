from sqlalchemy import update, select, null

from ..auth.schemas import UserRead, UserUpdate
from database.db import db
from database.models import User
from ..dependencies import object_as_dict


async def update_user(user_info: UserUpdate, user):
    for name, item in user_info.model_dump(exclude_none=True).items():
        setattr(user, name, item)

    it = object_as_dict(user).copy()
    user_id = it.pop("id")

    await db.sql_query(query=update(User).where(User.id == user_id).values(
        **it), is_update=True)

    return object_as_dict(user)
