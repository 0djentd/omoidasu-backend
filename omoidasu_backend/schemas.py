from pydantic import BaseModel


# ========= CARD ===========
class CardBase(BaseModel):
    question: str
    answer: str


class CardCreate(CardBase):
    pass


class Card(CardBase):
    id: int

    class Config:
        orm_mode = True


# ========= USER ===========
class UserBase(BaseModel):
    email: str


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    id: int
