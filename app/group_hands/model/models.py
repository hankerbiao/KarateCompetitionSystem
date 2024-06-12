# from sqlalchemy import JSON
from sqlmodel import SQLModel, Field
from typing import Optional, List, Generic, TypeVar
from core.enum import ColorEnum

T = TypeVar('T')


class Sites(SQLModel, table=True):
    """
    场地表
    """
    id: int = Field(default=None, primary_key=True)
    name: str = None  # 场地名称
    location: str = None  # 地点
    is_match_schedule_id: int = Field(default=None)  # 正在运行中的比赛


class Schedule(SQLModel, table=True):
    """
    组手赛程表
    """
    id: int = Field(default=None, primary_key=True)
    name: str = Field(default="")  # 赛程名称
    site_id: int = Field(default=None)  # 场地id
    red_id: int = Field(default=None)  # 红方id
    cyan_id: int = Field(default=None)  # 青方id
    status: Optional[int] = Field(default=0)  # 比赛状态 0-未开始 1-比赛中 2-比赛完成
    red_score: Optional[int] = Field(default=0)  # 红方得分
    red_foul: Optional[int] = Field(default=0)  # 红方犯规次数
    cyan_score: Optional[int] = Field(default=0)  # 青方得分
    cyan_foul: Optional[int] = Field(default=0)  # 青方犯规次数
    video_path: Optional[str] = Field(default=None)  # 视频保存地址
    winner_id: Optional[int] = Field(default=None)  # 获胜方ID
    preempt_id: Optional[int] = Field(default=0)  # 先取ID
    group: Optional[int] = Field(default=0)  # 组别


class Athlete(SQLModel, table=True):
    """
    运动员个人信息
    """
    id: int = Field(default=None, primary_key=True)
    name: str = Field(default="")  # 赛程名称
    unit: str = Field(default="")  # 单位名称
    group: int = Field(default=0)  # 组别
    status: int = Field(default=0)  # 状态： 0-未开始 1-比赛中 2-比赛完成
    place: int = Field(default=-1)  # 名次：-1 淘汰


class MatchScore(SQLModel):
    schedule_id: int = Field(default=None)  # 赛程id
    color: ColorEnum = Field(default=None)  # 选手颜色


class AthleteResponse(SQLModel):
    total: int
    athletes: List[Athlete]


class ResponseModel(Generic[T], SQLModel):
    status: bool = Field(default=True, description="请求是否成功")
    code: int = Field(default=200, description="状态码")
    data: Optional[T] = Field(default=None, description="响应数据")
    message: str = Field(default="成功", description="描述信息")
