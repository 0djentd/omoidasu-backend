from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from .. import crud, schemas, database

router = APIRouter(
        prefix="/users")


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()