from typing import List

from fastapi import APIRouter, HTTPException
from core.db import SessionDep
from app.group_hands.model.models import Athlete

router = APIRouter()


# 查询所有运动员
@router.get("/athlete/", response_model=List[Athlete])
def read_schedules(db: SessionDep, skip: int = 0, limit: int = 10):
    athletes = db.query(Athlete).offset(skip).limit(limit).all()
    return athletes


# 查询运动员根据id
@router.get("/athletes/{athlete_id}", response_model=Athlete)
def read_schedule(athlete_id: int, db: SessionDep):
    schedule = db.query(Athlete).filter(Athlete.id == athlete_id).first()
    if not schedule:
        raise HTTPException(status_code=404, detail="Athlete not found")
    return schedule


# 创建运动员
@router.post("/athletes/", response_model=Athlete)
def create_schedule(schedule: Athlete, db: SessionDep):
    db.add(schedule)
    db.commit()
    db.refresh(schedule)
    return schedule
