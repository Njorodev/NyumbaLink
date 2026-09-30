from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from routers import auth, properties

Base.metadata.create_all(bind=engine)

app = FastAPI(title="NyumbaLink API", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500", "http://localhost:5500",
        "http://127.0.0.1:8080", "http://localhost:8080"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(auth.router)
app.include_router(properties.router)

@app.get("/")
def root():
    return {"message": "NyumbaLink API is running"}

@app.get("/api/health")
def health():
    return {"status": "ok"}
