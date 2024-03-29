from datetime import datetime
from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import Column, String, Boolean, TIMESTAMP
from sqlalchemy.ext.asyncio import AsyncSession
from database.models import Base
from database.db import db


class User(SQLAlchemyBaseUserTable[int], Base):
    email = Column(String(60), nullable=False)
    nickname = Column(String, nullable=False)
    date_created = Column(TIMESTAMP, default=datetime.utcnow)
    telegram_tag = Column(String(60), nullable=True)
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)


async def get_user_db(session: AsyncSession = Depends(db.get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
