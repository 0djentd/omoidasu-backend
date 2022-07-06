from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import crud, database, schemas

router = APIRouter(
        prefix="/users")


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()