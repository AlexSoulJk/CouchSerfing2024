from fastapi_users import FastAPIUsers
from web.backend import router as primary_router
from web.backend.auth.auth import auth_backend

from fastapi import FastAPI

from web.backend.auth.auth_user import User
from web.backend.auth.manager import get_user_manager
from web.backend.auth.schemas import UserCreate, UserRead

app = FastAPI(title="couch_surfing")
app.include_router(prefix="/main", router=primary_router)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)