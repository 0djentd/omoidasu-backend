from pydantic import BaseModel


# ========= CARD ===========
class CardBase(BaseModel):
    question: str
    answer: str


class CardCreate(CardBase):
    pass


class Card(CardBase):
    id: int
    ok: int
    fail: int

    class Config:
        orm_mode = True


# ========= USER ===========
class UserBase(BaseModel):
    email: str


class UserIn(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
