from fastapi import APIRouter, Depends
from . import crud
from ..auth.schemas import UserRead
from ..rule.schemas import RuleCreate, RuleGet, CardRuleGet, CardRuleGetForChange, RuleForChange
from ..dependencies import get_room_by_id, get_user_by_token, is_room_owner
from ..room.schemas import RoomGet

router = APIRouter(tags=["Rules"])


@router.post("create/{room_id}/")
async def create_rules_in_room(rules: list[RuleCreate],
                               room: RoomGet = Depends(is_room_owner)):
    await crud.create_rule_in_room(rules=rules, room_id=room.id)


@router.get("/{room_id}/", response_model=list[RuleGet])
async def get_rules_by_room_id(room: RoomGet = Depends(get_room_by_id)):
    return await crud.get_rules_in_room(room_id=room.id)


@router.get("not_in/{room_id}/", response_model=list[RuleGet])
async def get_rules_not_in_room_by_id(room: RoomGet = Depends(get_room_by_id)):
    return await crud.get_rules_not_in_room(room_id=room.id)


# Запрос для получения всех правил комнаты.
# Доступен для авторизованного пользователя в момент создания комнаты
@router.get("/", response_model=list[CardRuleGet])
async def get_all_rules():
    return await crud.get_all_rules()


# TODO: Переписать
@router.delete("/{room_id}/")
async def delete_rules_in_room(rules: list[RuleCreate],
                               room: RoomGet = Depends(is_room_owner)):
    await crud.delete_rule_in_room_by_ids(rules=rules, room_id=room.id)


# Изменение правил комнаты для авторизованного пользователя.
@router.patch("/")
async def update_rules_in_room(rules: list[RuleForChange],
                               user: UserRead = Depends(get_user_by_token)):
    await crud.update_rules(rules=rules)


# Получение списка выбранных правил в комнате.
# Используется в момент изменения комнаты.
@router.post("change/{room_id}/", response_model=list[CardRuleGetForChange])
async def get_list_rules_for_change_by_room_id(room: RoomGet = Depends(is_room_owner)):
    return await crud.get_rules_in_room_for_change(room_id=room.id)
