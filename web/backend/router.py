from fastapi_users import FastAPIUsers

from fastapi import FastAPI, Depends

from web.backend.auth.auth import auth_backend
from web.backend.auth.auth_user import User
from web.backend.auth.manager import get_user_manager
from web.backend.auth.schemas import UserRead, UserCreate

app = FastAPI(
    title="CouchSurfing"
)

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

current_user = fastapi_users.current_user()

@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.nickname}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"
