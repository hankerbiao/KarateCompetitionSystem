from typing import Optional
from sqlmodel import SQLModel


class ScheduleUpdate(SQLModel):
    id: Optional[int] = None
    name: Optional[str] = None
    site_id: Optional[int] = None
    status: Optional[int] = None
    red_score: Optional[int] = None
    red_foul: Optional[int] = None
    cyan_score: Optional[int] = None
    cyan_foul: Optional[int] = None
    winner_id: Optional[int] = None
    preempt: Optional[int] = None
    video_path: Optional[str] = None
    red_id: Optional[int] = None
    cyan_id: Optional[int] = None
    red_name: Optional[str] = None  # 红方名称
    cyan_name: Optional[str] = None  # 青方名称
    red_unit: Optional[str] = None  # 红方单位
    cyan_unit: Optional[str] = None  # 青方单位
    site_name: Optional[str] = None  # 场地名称


class AthleteUpdate(SQLModel):
    name: Optional[str] = None
    unit: Optional[str] = None
    group: Optional[int] = None
    status: Optional[int] = None
    place: Optional[int] = None
