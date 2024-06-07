from fastapi import APIRouter
from core.db import SessionDep
from app.group_hands.model.models import Sites

router = APIRouter()


@router.get("/fields/{field_id}", response_model=Sites)
def read_field(field_id: int, db: SessionDep):
    """
    根据场地id查询场地信息
    """
    sites = db.get(Sites, field_id)
    if not sites:
        return Sites()
    return sites


@router.post("/fields", response_model=Sites)
def create_field(site: Sites, db: SessionDep):
    """
    创建场地
    """
    db_site = Sites(name=site.name, location=site.location)
    db.add(db_site)
    db.commit()
    db.refresh(db_site)
    return db_site
