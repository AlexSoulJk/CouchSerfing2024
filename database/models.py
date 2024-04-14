from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncAttrs

from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, declared_attr


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)


class User(Base):
    nickname = Column(String(100), nullable=False, unique=True)

    date_created = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    date_deleted = Column(Date, nullable=True)

    login = Column(String(100), nullable=False)

    hashed_password = Column(String(length=1024), nullable=False)

    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)

    email = Column(String(60), nullable=False)
    telegram_tag = Column(String(60), nullable=True)


class Room(Base):
    user_id = Column(Integer, ForeignKey("users.id"))

    date_created = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    date_disabled = Column(Date, nullable=True)
    date_deleted = Column(Date, nullable=True)

    description = Column(String(3000))
    price = Column(Integer)
    location = Column(String(100))




class Rule(Base):
    description = Column(String(100), nullable=False)
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
    user_id = Column(Integer, ForeignKey("users.id"))

    date_created = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    date_deleted = Column(Date, nullable=True)

    text = Column(String(400), nullable=False)


class Favorite(Base):
    user_id = Column(Integer, ForeignKey("users.id"))
    room_id = Column(Integer, ForeignKey("rooms.id"))

    date_created = Column(Date, nullable=False)
    date_deleted = Column(Date, nullable=True)


class Deal(Base):
    owner_id = Column(Integer, ForeignKey("users.id"))
    guest_id = Column(Integer, ForeignKey("users.id"))
    room_id = Column(Integer, ForeignKey("rooms.id"))

    date_created = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    date_closed = Column(Date, nullable=True)
    status = Column(Integer, nullable=False)
