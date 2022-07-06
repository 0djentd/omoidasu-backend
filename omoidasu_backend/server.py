from fastapi import APIRouter, FastAPI

from . import database
from .cards import router as cards_router
from .users import router as users_router

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
api_router = APIRouter(prefix="/api")
api_router.include_router(cards_router.router)
api_router.include_router(users_router.router)
app.include_router(api_router)
