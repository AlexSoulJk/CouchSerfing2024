from fastapi import APIRouter
from fastapi_users import FastAPIUsers
from web.backend.auth.auth import auth_backend
from web.backend.auth.auth_user import User
from web.backend.auth.manager import get_user_manager
from web.backend.auth.schemas import UserRead, UserCreate

auth_router = APIRouter()

fastapi_users_ = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

auth_routes = [
   fastapi_users_.get_auth_router(auth_backend),
   fastapi_users_.get_register_router(UserRead, UserCreate),
]

for route in auth_routes:
    auth_router.include_router(
        route,
        tags=["auth"],
    )

current_user = fastapi_users_.current_user()

# @app.get("/protected-route")
# def protected_route(user: User = Depends(current_user)):
#     return f"Hello, {user.nickname}"
#
#
# @app.get("/unprotected-route")
# def unprotected_route():
#     return f"Hello, anonym"
