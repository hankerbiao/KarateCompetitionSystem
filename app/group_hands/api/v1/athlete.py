from fastapi import APIRouter, HTTPException

from app.group_hands.schema.schema import AthleteUpdate
from core.db import SessionDep
from app.group_hands.model.models import Athlete, ResponseModel

router = APIRouter()


@router.get("/athlete/", response_model=ResponseModel)
def read_schedules(db: SessionDep):
    """
    查询所有运动员
    """
    athletes = db.query(Athlete).all()
    return ResponseModel(data=athletes)


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


@router.put("/athletes/{athlete_id}", response_model=Athlete)
def update_athlete(athlete_id: int, athlete_update: AthleteUpdate, db: SessionDep):
    """
    根据athlete_id更新对应运动员信息
    """
    db_athlete = db.query(Athlete).filter(Athlete.id == athlete_id).first()
    if not db_athlete:
        raise HTTPException(status_code=404, detail="Athlete not found")

    update_data = athlete_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_athlete, key, value)

    db.commit()
    db.refresh(db_athlete)
    return db_athlete
