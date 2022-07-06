from fastapi import APIRouter, Depends, FastAPI, HTTPException
from pydantic import BaseModel

from . import database
from .routers import cards as cards_router
from .routers import users as users_router

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
api_router = APIRouter(prefix="/api")
api_router.include_router(cards_router.router)
api_router.include_router(users_router.router)
app.include_router(api_router)
