from fastapi import APIRouter
from .. import database

router = APIRouter(
    prefix="/users")


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
