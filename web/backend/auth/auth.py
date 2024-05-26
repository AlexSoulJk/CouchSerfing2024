import os

from dotenv import load_dotenv
from fastapi_users.authentication import CookieTransport, AuthenticationBackend, BearerTransport
from fastapi_users.authentication import JWTStrategy

load_dotenv()
SECRET = os.getenv("db_url")

cookie_transport = CookieTransport(cookie_name="bonds", cookie_max_age=3600)


bearer_transport = BearerTransport(tokenUrl="/main/auth/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
