from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import database, schemas
from . import crud

router = APIRouter(
        prefix="/cards")


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.Card])
def get_list(db: Session = Depends(get_db)):
    return crud.get_list(db)


@router.post("/", response_model=schemas.Card)
def create(card: schemas.CardCreate, db: Session = Depends(get_db)):
    return crud.create(db, card)


@router.get("/{id}/", response_model=schemas.Card)
def get(id: int, db: Session = Depends(get_db)):
    return crud.get(db, id)


@router.patch("/{id}/", response_model=schemas.Card)
def update(id: int, card: schemas.CardCreate, db: Session = Depends(get_db)):
    return crud.update(db, id, card)


@router.delete("/{id}/")
def delete(id: int, db: Session = Depends(get_db)):
    return crud.delete(db, id)