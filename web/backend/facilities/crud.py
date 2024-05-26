import sqlalchemy
from sqlalchemy import delete, select, case, update

from database.db import db
from database.models import Facility as F
from database.models import RoomFacility
from web.backend.facilities.schemas import FacilityCreate, \
    FacilityGet, Facility, FacilityForChange, FacilityGetForChange
from fastapi import HTTPException, status
from ..dependencies import object_as_dict


async def create_facilities_in_room(facilities: list[FacilityCreate], room_id: int):
    dict_ = []
    for item in facilities:
        el = item.model_dump()
        el["room_id"] = room_id
        dict_.append(RoomFacility(**el))
        await db.create_objects(dict_)


async def delete_facilities_in_room_by_ids(facilities: list[FacilityCreate], room_id: int) -> None:
    ids = [item.facility_id for item in facilities]
    res = await db.delete(query=delete(RoomFacility).where(
        RoomFacility.room_id == room_id).where(RoomFacility.facility_id.in_(ids)))

    if res.rowcount == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"In room with id {room_id} some facility are not founded")


async def get_facilities_in_room(room_id: int):
    return await db.sql_query(query=select(F).join_from(
        RoomFacility, F).where(
        RoomFacility.room_id == room_id), single=False)


async def get_all_facilities():
    res = await db.sql_query(query=select(F),
                             single=False)
    return [FacilityGet(**object_as_dict(item)) for item in res]


async def get_facilities_in_room_for_change(room_id: int):
    def get_info():
        return [selected_ans.facility_id for selected_ans, _ in selected_answers], \
            dict([(quest_id, selected_ans.id)
                  for selected_ans, quest_id in selected_answers])

    selected_answers = await db.sql_query(
        query=select(RoomFacility, F.id)
        .join(F, RoomFacility.facility_id == F.id)
        .where(RoomFacility.room_id == room_id),
        single=False, is_scalars=False
    )

    selected_answers_id, selected_info = get_info()

    return [FacilityGetForChange(id=item.id,
                                 description=item.description,
                                 id_user_answer=selected_info.get(item.id),
                                 is_selected=selected_info.get(item.id) is None)
            for item in await db.sql_query(query=select(F),
                                           single=False)]


async def update_facilities(rules: list[FacilityForChange]):
    whens = [(RoomFacility.id == item.id_user_answer, item.facility_id) for item in rules]

    stmt = update(RoomFacility) \
        .where(RoomFacility.id
               .in_([item.id_user_answer for item in rules])) \
        .values(facility_id=case(*whens, else_=RoomFacility.facility_id))

    await db.sql_query(stmt, is_update=True)
