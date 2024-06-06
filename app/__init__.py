from fastapi import FastAPI
from sqlmodel import SQLModel
from app.group_hands.api import api_route
from core.config import settings
from core.db import engine


def create_app():
    app = FastAPI()

    @app.on_event("startup")
    def on_startup():
        SQLModel.metadata.create_all(engine)

    app.include_router(api_route, prefix=settings.API_V1_STR)
    return app
