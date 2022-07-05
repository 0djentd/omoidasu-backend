from sqlalchemy import Column, Integer, String

from .database import Base


class Card(Base):
    """Card db model."""
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    ok = Column(Integer, default=0)
    fail = Column(Integer, default=0)


class User(Base):
    """User db model."""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    hashed_password = Column(String)
