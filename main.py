from web.backend import router as primary_router

from fastapi import FastAPI

app = FastAPI(title="couch_surfing")
app.include_router(prefix="/main", router=primary_router)
