from typing import Optional

from web.backend.auth.schemas import UserRead
from web.backend.filter_for_rooms.schemas import StartFilter, MainFilter


async def get_start_list_for_user(user: Optional[UserRead],
                                  start_filter: StartFilter):
    if user is not None:
        # Написать запрос для сравнения по
        # правилам, которые установлены в комнате.

        # Написать запрос для фильтрации по other answers

        pass

    # Совместить стартовый фильтр с данными, которые получились по
    # информации из анкеты пользователя.

    pass


async def get_main_list_for_user(user: Optional[UserRead],
                                 start_filter: MainFilter):
    if user is not None:
        # Написать запрос для сравнения по
        # правилам, которые установлены в комнате.
        # Написать запрос для фильтрации по other answers

        pass

    # Совместить основным фильтр с данными, которые получились по
    # информации из анкеты пользователя учесть, что теперь приоритет
    # выделяется на пользовательские отметки.

    pass
