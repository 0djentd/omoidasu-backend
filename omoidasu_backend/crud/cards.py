from sqlalchemy.orm import Session

from .. import models, schemas


def create_card(db: Session, card: schemas.CardCreate):
    db_card = models.Card(**card.dict())
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card


def get_cards_list(db: Session):
    return db.query(models.Card).all()


def get_card_by_id(db: Session, card_id: int) -> models.Card:
    return db.query(models.Card).filter(models.Card.id == card_id).first()


def update_card(db: Session, card: schemas.CardCreate, card_id: int):
    db_card = get_card_by_id(db, card_id)
    db_card.question = card.question
    db_card.answer = card.answer
    db.commit()
    db.refresh(db_card)
    return db_card


def delete_card(db: Session, card_id: int):
    db_card = get_card_by_id(db, card_id)
    db.delete(db_card)
    db.commit()