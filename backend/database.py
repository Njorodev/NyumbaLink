import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Retrieve environment variables
TURSO_DATABASE_URL = os.getenv("TURSO_DATABASE_URL")
TURSO_AUTH_TOKEN = os.getenv("TURSO_AUTH_TOKEN")

# Use Turso if deployed on Vercel/configured with credentials; fallback to local SQLite for dev
if TURSO_DATABASE_URL and TURSO_AUTH_TOKEN:
    # Convert 'libsql://' or 'https://' to SQLAlchemy's sqlite + libsql format
    url_body = TURSO_DATABASE_URL.replace("libsql://", "").replace("https://", "")
    DATABASE_URL = f"sqlite+libsql://{url_body}?authToken={TURSO_AUTH_TOKEN}&secure=true"
    engine = create_engine(DATABASE_URL)
else:
    DATABASE_URL = "sqlite:///./nyumbalink.db"
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()