from fastapi import APIRouter
from .room.view import router as room_router
from .rule.view import router as rule_router
from .picture.view import router as picture_router
from .auth.router import auth_router
from .filter_for_rooms.views import router as f_router
from .questions_and_answers.views import router as q_and_a
from .facilities.view import router as facilities

router = APIRouter()
router.include_router(router=room_router, prefix="/rooms")
router.include_router(router=rule_router, prefix="/rules")
router.include_router(router=picture_router, prefix="/picture")
router.include_router(router=auth_router, prefix="/auth")
router.include_router(router=f_router, prefix="/filter")
router.include_router(router=q_and_a, prefix="/registration_form")
router.include_router(router=facilities, prefix="/facilities")
