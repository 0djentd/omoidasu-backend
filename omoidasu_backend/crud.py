from sqlalchemy.orm import Session

from . import models, schemas


# ========= CARD ===========
def create_card(db: Session, card: schemas.CardCreate):
    db_card = models.Card(**card.dict())
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card


def get_cards_list(db: Session):
    return db.query(models.Card).all()


def get_card_by_id(db: Session, card_id: int):
    return db.query(models.Card).filter(models.Card.id == card_id).first()
