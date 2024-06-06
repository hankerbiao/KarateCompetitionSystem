from typing import List, Optional
from fastapi import APIRouter, HTTPException

from app.group_hands.schema.schema import ScheduleUpdate
from core.db import SessionDep
from app.group_hands.model.models import Schedule, Athlete

router = APIRouter()


# 查询所有赛程实例
@router.get("/schedules/", response_model=List[Schedule])
def read_schedules(db: SessionDep, skip: int = 0, limit: int = 10, site_id: Optional[int] = None):
    """
    site_id = None，查询所有赛程
    根据site_id查询对应场地的所有赛程
    """
    query = db.query(Schedule)  # 查询所有赛程信息

    if site_id is not None:
        query = query.filter(Schedule.site_id == site_id)

    schedules: List[Schedule] = query.offset(skip).limit(limit).all()

    return schedules


# 通过 ID 查询赛程实例
@router.get("/schedules/{schedule_id}", response_model=Schedule)
def read_schedule(schedule_id: int, db: SessionDep):
    schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if not schedule:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return schedule


# 创建新的 赛程 实例
@router.post("/schedules/", response_model=Schedule)
def create_schedule(schedule: Schedule, db: SessionDep):
    """
    创建新的赛程
    """
    db.add(schedule)
    db.commit()
    db.refresh(schedule)
    return schedule


# 根据赛程id更新赛程实例
@router.put("/schedules/{schedule_id}", response_model=Schedule)
def update_schedule(schedule_id: int, schedule_update: ScheduleUpdate, db: SessionDep):
    """
    根据schedule_id更新对应赛程信息
    """
    db_schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if not db_schedule:
        raise HTTPException(status_code=404, detail="Schedule not found")

    update_data = schedule_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_schedule, key, value)

    db.commit()
    db.refresh(db_schedule)
    return db_schedule
