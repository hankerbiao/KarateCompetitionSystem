from fastapi import APIRouter
from core.db import SessionDep
from app.group_hands.model.models import Site, ResponseModel

router = APIRouter()


@router.get("/fields/", response_model=ResponseModel)
def read_field(db: SessionDep):
    """
    获取所有组件信息
    """
    sites = db.query(Site).all()
    if not sites:
        return Site()
    return ResponseModel(data=sites)


@router.get("/fields/{field_id}", response_model=Site)
def read_field(field_id: int, db: SessionDep):
    """
    根据场地id查询场地信息
    """
    sites = db.get(Site, field_id)
    if not sites:
        return Site()
    return sites


@router.post("/fields", response_model=Site)
def create_field(site: Site, db: SessionDep):
    """
    创建场地
    """
    db_site = Site(name=site.name, location=site.location)
    db.add(db_site)
    db.commit()
    db.refresh(db_site)
    return db_site
