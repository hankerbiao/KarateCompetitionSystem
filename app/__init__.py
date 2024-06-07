from fastapi import FastAPI
from sqlmodel import SQLModel
from starlette.middleware.cors import CORSMiddleware

from app.group_hands.api import api_route
from core.config import settings
from core.db import engine


def create_app():
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],  # List of allowed origins
        allow_credentials=True,
        allow_methods=["*"],  # List of allowed methods
        allow_headers=["*"],  # List of allowed headers
    )

    @app.on_event("startup")
    def on_startup():
        SQLModel.metadata.create_all(engine)

    app.include_router(api_route, prefix=settings.API_V1_STR)
    return app
