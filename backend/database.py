import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

TURSO_DATABASE_URL = os.getenv("TURSO_DATABASE_URL")
TURSO_AUTH_TOKEN = os.getenv("TURSO_AUTH_TOKEN")

if TURSO_DATABASE_URL and TURSO_AUTH_TOKEN:
    # 1. Ensure URL uses the sqlite+libsql dialect scheme
    # 2. Strip any existing protocol prefix or trailing slash
    raw_host = (
        TURSO_DATABASE_URL.replace("libsql://", "")
        .replace("https://", "")
        .rstrip("/")
    )

    # Format explicitly with authToken query param
    DATABASE_URL = f"sqlite+libsql://{raw_host}?authToken={TURSO_AUTH_TOKEN}"

    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False},
        pool_pre_ping=True,
    )
else:
    DATABASE_URL = "sqlite:///./nyumbalink.db"
    engine = create_engine(
        DATABASE_URL, connect_args={"check_same_thread": False}
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()