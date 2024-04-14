from fastapi import APIRouter
from .room.view import router as room_router

router = APIRouter()
router.include_router(router=room_router, prefix="/rooms")
