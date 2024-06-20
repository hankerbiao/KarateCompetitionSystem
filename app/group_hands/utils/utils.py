from functools import lru_cache
from typing import Tuple

from app.group_hands.model.models import Athlete, Site
from core.db import SessionDep


# 通过运动员ID，查询运动员名称
@lru_cache(maxsize=100)
def get_athlete_name(athlete_id: int, db: SessionDep) -> Tuple[str, str]:
    """
    通过运动员ID，查询运动员名称和单位
    """
    athlete = db.query(Athlete).filter(Athlete.id == athlete_id).first()
    if not athlete:
        return ("", "")
    return athlete.name, athlete.unit


# 通过场地ID，查询场地名称
@lru_cache(maxsize=100)
def get_site_name(site_id: int, db: SessionDep) -> str:
    """

    :param site_id:
    :param db:
    :return:
    """
    site = db.query(Site).filter(Site.id == site_id).first()
    if not site:
        return ""
    return site.name
