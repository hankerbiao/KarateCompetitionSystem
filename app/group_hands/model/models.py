from sqlmodel import SQLModel, Field
from typing import Optional

from core.enum import ColorEnum


class Sites(SQLModel, table=True):
    """
    场地表
    """
    id: int = Field(default=None, primary_key=True)
    name: str = None  # 场地名称
    location: str = None  # 地点
    # todo 当前场地运行的比赛


class Schedule(SQLModel, table=True):
    """
    组手赛程表
    """
    id: int = Field(default=None, primary_key=True)
    name: str = Field(default="")  # 赛程名称
    site_id: int = Field(default=None)  # 场地id
    status: int = Field(default=0)  # 比赛状态 0-未开始 1-比赛中 2-比赛完成
    red_score: int = Field(default=0)  # 红方得分
    red_foul: int = Field(default=0)  # 红方犯规次数
    cyan_score: int = Field(default=0)  # 青方得分
    cyan_foul: int = Field(default=0)  # 青方犯规次数
    video_path: str = Field(default=None)  # 视频保存地址
    red_id: int = Field(default=None)  # 红方id
    cyan_id: int = Field(default=None)  # 青方id
    red_name: Optional[str] = Field(default=None)  # 红方名称
    cyan_name: Optional[str] = Field(default=None)  # 青方名称
    red_unit: Optional[str] = Field(default=None)  # 红方单位
    cyan_unit: Optional[str] = Field(default=None)  # 青方单位
    winner_id: int = Field(default=None)  # 获胜方ID


class Athlete(SQLModel, table=True):
    """
    运动员个人信息
    """
    id: int = Field(default=None, primary_key=True)
    name: str = Field(default="")  # 赛程名称
    unit: str = Field(default="")  # 单位名称
    status: int = Field(default=0)  # 状态： 0-未开始 1-比赛中 2-比赛完成
    place: int = Field(default=-1)  # 名次：-1 淘汰


class MatchScore(SQLModel):
    schedule_id: int = Field(default=None)  # 赛程id
    color: ColorEnum = Field(default=None)  # 选手颜色
