from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from . import database, models, crud, schemas

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ========= /api/cards/ ===========
@app.get("/api/cards/", response_model=list[schemas.Card])
def cards_list(db: Session = Depends(get_db)):
    return crud.get_cards_list(db)


@app.post("/api/cards/", response_model=schemas.Card)
def cards_create(card: schemas.CardCreate, db: Session = Depends(get_db)):
    return crud.create_card(db, card)


@app.get("/api/cards/{id}/", response_model=schemas.Card)
def cards_get(id: int, db: Session = Depends(get_db)):
    return crud.get_card_by_id(db, id)
