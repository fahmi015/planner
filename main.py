from fastapi import FastAPI
from app.routers.auth import router as auth
from app.routers.api import router as api
from app.models.database import Base,engine
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)
origins = [
    "http://localhost:5173",
    "http://localhost",
    "http://localhost:8080",
    "http://app.superappcanari.com",
    "https://app.superappcanari.com"
]
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth)
app.include_router(api)
