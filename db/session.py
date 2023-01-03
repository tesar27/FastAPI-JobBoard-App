from typing import Generator

from core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///job-board.db", connect_args={'timeout': 15, "check_same_thread": False})

SessionLocal = sessionmaker(
    autocommit=False, expire_on_commit=False,
    autoflush=False, bind=engine
)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
