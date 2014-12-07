from connection import Base
from sqlalchemy import Colomn, Integer, String


class MathProblems(Base):
    __table__ = 'math_problems'
    id = Colomn(Integer, primary_key=True)
    problem = Colomn(String)
    answer = Colomn(String)
    