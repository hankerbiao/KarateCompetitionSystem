from typing import List, Optional
from fastapi import APIRouter, HTTPException

from app.group_hands.schema.schema import ScheduleUpdate
from app.group_hands.utils.utils import get_athlete_name, get_site_name
from core.constants import SCHEMA_NAME_LIST
from core.db import SessionDep
from app.group_hands.model.models import Schedule, ResponseModel

router = APIRouter()


@router.get('/schedules/schedules_name_list', response_model=ResponseModel)
def get_schedules_name_list():
    """
    获取所有赛程名称
    """
    return ResponseModel(data=SCHEMA_NAME_LIST)


# 查询所有赛程实例
@router.get("/schedules/", response_model=ResponseModel)
def read_schedules(db: SessionDep, site_id: Optional[int] = None):
    """
    site_id = None，查询所有赛程
    根据site_id查询对应场地的所有赛程
    """
    query = db.query(Schedule)  # 查询所有赛程信息

    if site_id is not None:
        query = query.filter(Schedule.site_id == site_id)
    response_schedules = []
    schedules = query.all()
    for schedule in schedules:
        response_schedule = ScheduleUpdate(
            **schedule.__dict__,
            red_name=get_athlete_name(schedule.red_id, db)[0],
            red_unit=get_athlete_name(schedule.red_id, db)[1],
            cyan_name=get_athlete_name(schedule.cyan_id, db)[0],
            cyan_unit=get_athlete_name(schedule.cyan_id, db)[1],
            site_name=get_site_name(schedule.site_id, db)
        )
        response_schedules.append(response_schedule)
    return ResponseModel(data=response_schedules)


@router.get("/schedules/{schedule_id}", response_model=Schedule)
def read_schedule(schedule_id: int, db: SessionDep):
    """
    通过 ID 查询赛程实例
    """
    schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if not schedule:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return schedule


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


# 删除赛程接口
@router.delete("/schedules/{schedule_id}", response_model=Schedule)
def delete_schedule(schedule_id: int, db: SessionDep):
    """
    根据schedule_id删除对应赛程
    """
    schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if not schedule:
        raise HTTPException(status_code=404, detail="Schedule not found")

    db.delete(schedule)
    db.commit()
    return schedule
