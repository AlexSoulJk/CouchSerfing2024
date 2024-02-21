import logging
import os

from dotenv import load_dotenv

from sqlalchemy import create_engine, select, update, delete, Engine, literal_column, join

from sqlalchemy.orm import sessionmaker

from database import models


class Database:
    def __init__(self, db_url):
        self.session_maker = None
        self.url = db_url
        self.engine = None

    def connect(self):

        try:
            self.engine = create_engine(self.url)
            self.session_maker = sessionmaker(bind=self.engine)
            self.sql_query(query=select(1))
            logging.info("Database connected")
        except Exception as e:
            logging.error(e)
            logging.error("Database didn't connect")

    def sql_query(self, query, is_single=True, is_update=False):
        with self.session_maker(expire_on_commit=True) as session:
            response = session.execute(query)
            if not is_update:
                return response.scalars().first() if is_single else response.all()
            session.commit()

    def create_object(self, model):
        with self.session_maker(expire_on_commit=True) as session:
            session.add(model)
            session.commit()


load_dotenv()
logging.basicConfig(level=logging.INFO)
db = Database(os.getenv("db_url"))
db.connect()
