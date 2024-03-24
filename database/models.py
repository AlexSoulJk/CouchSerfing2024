import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncAttrs

from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy_utils import StringEncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import AesEngine

load_dotenv()
secret_key = os.getenv("secret_key_sql")


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)


class User(Base):
    nickname = Column(String(100), nullable=False, unique=True)

    date_created = Column(Date, nullable=False)
    date_deleted = Column(Date, nullable=True)

    login = Column(StringEncryptedType(String(100), secret_key, AesEngine,
                                       'pkcs5', length=100), nullable=False)

    password = Column(StringEncryptedType(String(100), secret_key, AesEngine,
                                          'pkcs5', length=100), nullable=False)

    email = Column(String(60), nullable=False)
    telegram_tag = Column(String(60), nullable=True)


class Room(Base):
    user_id = Column(Integer, ForeignKey("users.id"))

    date_created = Column(Date, nullable=False)
    date_disabled = Column(Date, nullable=True)
    date_deleted = Column(Date, nullable=True)

    description = Column(String(3000))


class Rule(Base):
    description = Column(String(100), nullable=False)
    url_pic = Column(String(100), nullable=False)


class RoomRule(Base):
    room_id = Column(Integer, ForeignKey("rooms.id"))
    rule_id = Column(Integer, ForeignKey("rules.id"))


class RoomPicture(Base):
    room_id = Column(Integer, ForeignKey("rooms.id"))

    date_created = Column(Date, nullable=False)
    date_disabled = Column(Date, nullable=True)

    url_picture = Column(String(100), nullable=False)


class Notification(Base):
    user_id = Column(Integer, ForeignKey("users.id"))

    date_created = Column(Date, nullable=False)
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

    date_created = Column(Date, nullable=False)
    date_closed = Column(Date, nullable=True)
    status = Column(Integer, nullable=False)
