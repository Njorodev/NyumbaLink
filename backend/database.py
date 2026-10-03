import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

TURSO_DATABASE_URL = os.getenv("TURSO_DATABASE_URL")
TURSO_AUTH_TOKEN = os.getenv("TURSO_AUTH_TOKEN")

if TURSO_DATABASE_URL and TURSO_AUTH_TOKEN:
    # Format: sqlite+libsql://<your-db-name>.turso.io?authToken=<token>&secure=true
    url_body = TURSO_DATABASE_URL.replace("libsql://", "").replace("https://", "").rstrip("/")
    DATABASE_URL = f"sqlite+libsql://{url_body}?authToken={TURSO_AUTH_TOKEN}&secure=true"
    
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False}
    )
else:
    DATABASE_URL = "sqlite:///./nyumbalink.db"
    engine = create_engine(
        DATABASE_URL, 
        connect_args={"check_same_thread": False}
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()