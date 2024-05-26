from typing import Optional

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from database.db import db
from web.backend import router as primary_router
from web.backend.auth.schemas import UserRead
from web.backend.dependencies import get_current_user_by_token

app = FastAPI(title="couch_surfing")

origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:63343",
    "http://127.0.0.1:63343",
    "http://localhost:63343/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(prefix="/main", router=primary_router)


@app.on_event("startup")
async def startup_event():
    await db.setup()


@app.post("/main/auth/logout")
def logout():
    # Просто возвращаем успешный ответ
    return {"message": "Logged out successfully"}


# Временный эндпоинт для тестирования
@app.get("/test_current_user")
async def test_current_user(user: Optional[UserRead] = Depends(get_current_user_by_token)):
    if user:
        return {"user_id": user.id, "email": user.email}
    return {"error": "User not authenticated"}
