from typing import List

from fastapi import APIRouter, HTTPException
from core.db import SessionDep
from app.group_hands.model.models import Athlete

router = APIRouter()


@router.get("/athlete/", response_model=List[Athlete])
def read_schedules(db: SessionDep, skip: int = 0, limit: int = 10):
    """
    查询所有运动员
    """
    athletes = db.query(Athlete).offset(skip).limit(limit).all()
    return athletes


@router.get("/athletes/{athlete_id}", response_model=Athlete)
def read_schedule(athlete_id: int, db: SessionDep):
    """
    根据运动员id查询
    """
    schedule = db.query(Athlete).filter(Athlete.id == athlete_id).first()
    if not schedule:
        raise HTTPException(status_code=404, detail="Athlete not found")
    return schedule


@router.post("/athletes/", response_model=Athlete)
def create_schedule(schedule: Athlete, db: SessionDep):
    """
    创建运动员
    """
    db.add(schedule)
    db.commit()
    db.refresh(schedule)
    return schedule
