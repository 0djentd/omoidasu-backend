import sqlalchemy

from sqlalchemy import Column, Integer, String
from .database import Base


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    hashed_password = Column(String)
