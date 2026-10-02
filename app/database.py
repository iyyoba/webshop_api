
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_PASSWORD = os.getenv("DB_PASSWORD")

DATABASE_URL = (
    f"mysql+pymysql://db_user:{DB_PASSWORD}"
    "@localhost:3306/DB_solutions"
)

engine = create_engine(
    DATABASE_URL,
    echo=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
