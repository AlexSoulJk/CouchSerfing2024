import asyncio
import logging
import os
from typing import AsyncGenerator

from dotenv import load_dotenv

from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker


class Database:
    def __init__(self, db_url: str):
        self.db_url = db_url
        self.__engine = create_async_engine(self.db_url)

    async def create_object(self, model, **attributes):
        # await self.connect()
        async with AsyncSession(self.__engine, expire_on_commit=False) as session:
            object = model(**attributes)
            session.add(object)
            await session.commit()
            return object

    async def create_objects(self, model_s: []):
        async with AsyncSession(self.__engine, expire_on_commit=True) as session:
            session.add_all(model_s)
            await session.commit()

    async def sql_query(self, query, single=True, is_scalars = True, is_update=False, *args, **kwargs):
        async with AsyncSession(self.__engine) as session:
            result = await session.execute(query)
            if not is_update:
                if is_scalars:
                    return result.scalars().first() if single else result.scalars().all()
                else:
                    return result.first() if single else result.all()
            await session.commit()
            return result

    async def delete(self, query):
        async with AsyncSession(self.__engine) as session:
            result = await session.execute(query)
            await session.commit()
            return result

    async def get_async_session(self) -> AsyncGenerator[AsyncSession, None]:
        async_session_maker = sessionmaker(self.__engine, class_=AsyncSession, expire_on_commit=False)
        async with async_session_maker() as session:
            yield session

    async def connect(self):
        self.__engine = create_async_engine(self.db_url)
        await self.sql_query(query=select(1))
        logging.info("Database has been connected")

    async def check_and_initialize_data(self):

        # добавьте здесь свой код для проверки и инициализации данных
        pass

    async def disconnect(self):
        if self.__engine:
            await self.__engine.dispose()
        logging.info("Database has been disconnected")

    async def setup(self):
        await self.connect()
        await self.check_and_initialize_data()


load_dotenv()
logging.basicConfig(level=logging.INFO)
db = Database(os.getenv("db_url"))
# asyncio.run(db.setup())

# async def main():
#     load_dotenv()
#     logging.basicConfig(level=logging.INFO)
#     db = Database(os.getenv("db_url"))
#     await db.connect()
#     await db.disconnect()
#
# asyncio.run(main())
