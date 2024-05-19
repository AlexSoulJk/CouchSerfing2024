from typing import Annotated

from fastapi import FastAPI, Depends
from .models.schemas import SUserAdd
app = FastAPI()

users = []


@app.post("/user")
def get_task(user: Annotated[SUserAdd, Depends()]):
    users.append(user)
    return "task"
