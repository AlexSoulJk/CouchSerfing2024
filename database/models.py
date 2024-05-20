from datetime import datetime

from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.ext.asyncio import AsyncAttrs

from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, declared_attr
from fastapi_users.db import SQLAlchemyBaseUserTable


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "user"
    email = Column(String(60), nullable=False)
    nickname = Column(String, nullable=False)
    date_created = Column(TIMESTAMP, default=datetime.utcnow)
    telegram_tag = Column(String(60), nullable=True)
    login = Column(String(100), nullable=False)
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)
    date_deleted = Column(Date, nullable=True)


class Room(Base):
    user_id = Column(Integer, ForeignKey("user.id"))

    date_created = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    date_disabled = Column(Date, nullable=True)
    date_deleted = Column(Date, nullable=True)

    description = Column(String(3000))
    price = Column(Integer)
    location = Column(String(100))


class QuestionRule(Base):
    description_rule = Column(String(100), nullable=False)
    description_interest = Column(String(100), nullable=False)


class Rule(Base):
    room_rule_id = Column(Integer, ForeignKey("questionrules.id"))
    description_rule = Column(String(100), nullable=False)
    description_interest = Column(String(100), nullable=False)
    url_pic = Column(String(100), nullable=False)


class RoomRule(Base):
    room_id = Column(Integer, ForeignKey("rooms.id"))
    rule_id = Column(Integer, ForeignKey("rules.id"))


class RoomPicture(Base):
    room_id = Column(Integer, ForeignKey("rooms.id"))

    date_created = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    date_disabled = Column(Date, nullable=True)

    url_picture = Column(String(100), nullable=False)


class Notification(Base):
    user_id = Column(Integer, ForeignKey("user.id"))

    date_created = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    date_deleted = Column(Date, nullable=True)

    text = Column(String(400), nullable=False)


class Favorite(Base):
    user_id = Column(Integer, ForeignKey("user.id"))
    room_id = Column(Integer, ForeignKey("rooms.id"))

    date_created = Column(Date, nullable=False)
    date_deleted = Column(Date, nullable=True)


class Deal(Base):
    owner_id = Column(Integer, ForeignKey("user.id"))
    guest_id = Column(Integer, ForeignKey("user.id"))
    room_id = Column(Integer, ForeignKey("rooms.id"))

    date_created = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    date_closed = Column(Date, nullable=True)
    status = Column(Integer, nullable=False)


class UserAnswerRule(Base):
    user_id = Column(Integer, ForeignKey('user.id'))
    answer_id = Column(Integer, ForeignKey("rules.id"))


class QuestionOther(Base):
    description = Column(String(100), nullable=False)


class AnswerOther(Base):
    question_other_id = Column(Integer, ForeignKey('questionothers.id'))
    description = Column(String(100), nullable=False)


class UserAnswerOther(Base):
    user_id = Column(Integer, ForeignKey('user.id'))
    answer_other_id = Column(Integer, ForeignKey('answerothers.id'))
