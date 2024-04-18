
import os

from dotenv import load_dotenv

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy_utils import StringEncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import AesEngine




load_dotenv()
Base = declarative_base()
secret_key = os.getenv("secret_key_sql")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)

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
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    date_created = Column(Date, nullable=False)
    date_disabled = Column(Date, nullable=True)
    date_deleted = Column(Date, nullable=True)

    description = Column(String(3000))


class Rule(Base):
    __tablename__ = 'rules'

    id = Column(Integer, primary_key=True)

    description = Column(String(100), nullable=False)
    url_pic = Column(String(100), nullable=False)


class RoomRules(Base):
    __tablename__ = 'roomrules'

    id = Column(Integer, primary_key=True)
    room_id = Column(Integer, ForeignKey("rooms.id"))
    rule_id = Column(Integer, ForeignKey("rules.id"))


class RoomPictures(Base):
    __tablename__ = 'roompictures'

    id = Column(Integer, primary_key=True)
    room_id = Column(Integer, ForeignKey("rooms.id"))

    date_created = Column(Date, nullable=False)
    date_disabled = Column(Date, nullable=True)

    url_picture = Column(String(100), nullable=False)


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    date_created = Column(Date, nullable=False)
    date_deleted = Column(Date, nullable=True)

    text = Column(String(400), nullable=False)


class Favorite(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    room_id = Column(Integer, ForeignKey("rooms.id"))

    date_created = Column(Date, nullable=False)
    date_deleted = Column(Date, nullable=True)


class Deal(Base):
    __tablename__ = "deals"

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    guest_id = Column(Integer, ForeignKey("users.id"))
    room_id = Column(Integer, ForeignKey("rooms.id"))

    date_created = Column(Date, nullable=False)
    date_closed = Column(Date, nullable=True)
    status = Column(Integer, nullable=False)