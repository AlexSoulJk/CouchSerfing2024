import os

from dotenv import load_dotenv

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean, Unicode
from sqlalchemy.dialects.mysql import JSON
from sqlalchemy_utils import StringEncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import AesEngine

load_dotenv()
Base = declarative_base()
secret_key = os.getenv("secret_key_sql")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)

    nickname = Column(String(100))
    date_start = Column(Date, nullable=False)
    login = Column(StringEncryptedType(String(100), secret_key, AesEngine,
                                       'pkcs5', length=100), nullable=False)
    password = Column(StringEncryptedType(String(100), secret_key, AesEngine,
                                          'pkcs5', length=100), nullable=False)