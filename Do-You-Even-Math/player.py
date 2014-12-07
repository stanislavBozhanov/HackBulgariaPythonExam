from connection import Base
from sqlalchemy import Colomn, Integer, String


class Player(Base):
    __table__ = 'player'
    id = Colomn(Integer, primary_key=True)
    name = Colomn(String)
    score = Colomn(Integer)
