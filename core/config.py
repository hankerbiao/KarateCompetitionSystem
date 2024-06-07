import secrets
from pydantic.v1 import BaseSettings

import os


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"  # 路由前缀
    SECRET_KEY: str = secrets.token_urlsafe(32)
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    DATABASE_URL = 'sqlite:///' + os.path.join(BASE_DIR, 'data', 'karate.db')


settings = Settings()
