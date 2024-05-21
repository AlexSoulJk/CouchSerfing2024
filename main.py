from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from web.backend import router as primary_router
from database.db import db

app = FastAPI(title="couch_surfing")
app.include_router(prefix="/main", router=primary_router)

# @app.on_event("startup")
# async def startup_event():
#     await db.setup()

origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
