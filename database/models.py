from datetime import datetime

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


# Вопросы, которые выдаются пользователю при добавлении комнаты (правила).
class QuestionRoomRule(Base):
    description = Column(String(100), nullable=False)


# Правила(возможные варианты ответа на вопрос из QuestionRoomRule)
# для комнаты
class Rule(Base):
    quest_id = Column(Integer, ForeignKey("questionroomrules.id"))
    description = Column(String(100), nullable=False)
    url_pic = Column(String(100), nullable=False)


# Правила комнаты, которые пользователь выбрал из предложенных.
class RoomRule(Base):
    room_id = Column(Integer, ForeignKey("rooms.id"))
    rule_id = Column(Integer, ForeignKey("rules.id"))


class RoomPicture(Base):
    room_id = Column(Integer, ForeignKey("rooms.id"))

    date_created = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    date_disabled = Column(Date, nullable=True)

    url_picture = Column(String(100), nullable=False)
    is_front = Column(Boolean, nullable=True)


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


# Вопросы, для формы регистрации, которые мэтчатся
# с некоторыми правилами комнат.
class QuestionRule(Base):
    description = Column(String(100), nullable=False)


# Возможные ответы, для формы регистрации, которые мэтчатся
# с некоторыми правилами комнат.
class AnswerRule(Base):
    quest_id = Column(Integer, ForeignKey("questionrules.id"))
    rule_id = Column(Integer, ForeignKey("rules.id"))
    description = Column(String(100), nullable=False)


# Ответы, для формы регистрации, которые мэтчатся
# с некоторыми правилами комнат.
class UserAnswerRule(Base):
    user_id = Column(Integer, ForeignKey('user.id'))
    answer_id = Column(Integer, ForeignKey("answerrules.id"))


# Вопросы, для формы регистрации,
# которые не связаны с правилами комнат.
class QuestionOther(Base):
    description = Column(String(100), nullable=False)


# Возможные ответы на вопросы, для формы регистрации,
# которые не связаны с правилами комнат.
class AnswerOther(Base):
    question_other_id = Column(Integer, ForeignKey('questionothers.id'))
    description = Column(String(100), nullable=False)


# Ответы на вопросы, не связанные с правилами комнат,
# которые выбрал пользователь при регистрации,

class UserAnswerOther(Base):
    user_id = Column(Integer, ForeignKey('user.id'))
    answer_other_id = Column(Integer, ForeignKey('answerothers.id'))
