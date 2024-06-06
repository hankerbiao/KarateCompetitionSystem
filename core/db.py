from sqlmodel import create_engine, Session
from core.config import settings
from collections.abc import Generator
from typing import Annotated
from fastapi import Depends

engine = create_engine(settings.DATABASE_URL)


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]  # 别名，简化依赖关系的声明
