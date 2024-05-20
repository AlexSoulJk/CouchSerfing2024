from fastapi import APIRouter
from .room.view import router as room_router
from .rule.view import router as rule_router
from .picture.view import router as picture_router
from .auth.router import auth_router

router = APIRouter()
router.include_router(router=room_router, prefix="/rooms")
router.include_router(router=rule_router, prefix="/rules")
router.include_router(router=picture_router, prefix="/picture")
router.include_router(router=auth_router, prefix="/auth")
