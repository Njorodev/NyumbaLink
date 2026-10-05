import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

TURSO_DATABASE_URL = os.getenv("TURSO_DATABASE_URL")
TURSO_AUTH_TOKEN = os.getenv("TURSO_AUTH_TOKEN")

if TURSO_DATABASE_URL and TURSO_AUTH_TOKEN:

    # Turso should provide a URL such as:
    # libsql://your-database-your-org.turso.io
    #
    # Remove only the libsql:// prefix because SQLAlchemy's
    # dialect will add sqlite+libsql:// itself.

    raw_host = TURSO_DATABASE_URL.replace("libsql://", "").rstrip("/")

    DATABASE_URL = f"sqlite+libsql://{raw_host}?secure=true"

    engine = create_engine(
        DATABASE_URL,
        connect_args={
            "auth_token": TURSO_AUTH_TOKEN,
        },
        pool_pre_ping=True,
    )
else:
    # Local development
    DATABASE_URL = "sqlite:///./nyumbalink.db"
    engine = create_engine(
        DATABASE_URL,
        connect_args={
            "check_same_thread": False
        },
    )

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()