from sqlalchemy import create_engine
from sqlalchemy.orm import (
    sessionmaker,
    declarative_base
)

from api.config import (
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_NAME,
    DB_PORT
)

DATABASE_URL=(
"mysql+mysqlconnector://"
f"{DB_USER}:{DB_PASSWORD}"
f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base= declarative_base()