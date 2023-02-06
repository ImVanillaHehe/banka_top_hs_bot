from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = "postgresql://mykyta:1234@localhost:5432/leaderboard"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True
)
SessionLocal = Session(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()




