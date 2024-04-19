from datetime import datetime
from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import Column, String, Boolean, TIMESTAMP
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import db
from database.models import User



async def get_user_db(session: AsyncSession = Depends(db.get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
