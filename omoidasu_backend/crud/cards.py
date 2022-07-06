import logging

from sqlalchemy.orm import Session

from .. import models, schemas

logger = logging.getLogger(__name__)

def create_card(db: Session, card: schemas.CardCreate):
    # TODO
    db_card = models.Card(**card.dict(), user_id=0)
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card


def get_cards_list(db: Session):
    return db.query(models.Card).all()


def get_card_by_id(db: Session, card_id: int) -> models.Card:
    return db.query(models.Card).filter(models.Card.id == card_id).first()


def update_card(db: Session, card_id: int, card: schemas.CardCreate):
    db_card = get_card_by_id(db, card_id)
    if not db_card:
        return None
    db_card.question = card.question
    db_card.answer = card.answer
    db_card.ok = card.ok
    db_card.fail = card.fail
    db.commit()
    db.refresh(db_card)
    return db_card


def delete_card(db: Session, card_id: int):
    db_card = get_card_by_id(db, card_id)
    db.delete(db_card)
    db.commit()