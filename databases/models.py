from database import Base
from sqlalchemy import Column, String, Integer


class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    account_name = Column(String)
    rating = Column(Integer)
    rank = Column(Integer)


