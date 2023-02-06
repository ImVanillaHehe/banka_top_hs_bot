from database import Base
from sqlalchemy import Column, String, Integer


class Lead(Base):
    __tablename__ = "leaderboard"

    id = Column(Integer, primary_key=True)
    player_name = Column("player name", String)
    rating = Column("rating", Integer)
    rank = Column("rank", Integer)


