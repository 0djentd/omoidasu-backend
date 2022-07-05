from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from .. import schemas, database
from ..crud import cards as crud

router = APIRouter(
        prefix="/cards")


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.Card])
def cards_list(db: Session = Depends(get_db)):
    return crud.get_cards_list(db)


@router.post("/", response_model=schemas.Card)
def cards_create(card: schemas.CardCreate, db: Session = Depends(get_db)):
    return crud.create_card(db, card)


@router.get("/{id}/", response_model=schemas.Card)
def cards_get(id: int, db: Session = Depends(get_db)):
    return crud.get_card_by_id(db, id)


@router.patch("/{id}/", response_model=schemas.Card)
def cards_update(id: int, card: schemas.CardCreate, db: Session = Depends(get_db)):
    return crud.update_card(db, id, card)


@router.delete("/{id}/")
def cards_delete(id: int, db: Session = Depends(get_db)):
    return crud.delete_card(db, id)