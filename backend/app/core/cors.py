from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from .config import settings


def setup_cors(app: FastAPI):
    origins = [settings.FRONTEND_ORIGIN]
    if settings.FRONTEND_ORIGIN != "*":
        origins.extend(["http://localhost:3000", "http://127.0.0.1:3000"])
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins if settings.FRONTEND_ORIGIN != "*" else ["*"],
        allow_credentials=True,
        allow_methods=["GET", "POST", "PATCH", "DELETE", "OPTIONS"],
        allow_headers=["*"],
    )
