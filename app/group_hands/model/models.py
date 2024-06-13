from sqlmodel import SQLModel, Field
from typing import Optional, Generic, TypeVar

T = TypeVar('T')


class Site(SQLModel, table=True):
    """
    场地表
    """
    id: Optional[int] = Field(default=None, primary_key=True, description="唯一标识符")
    name: Optional[str] = Field(default=None, description="场地名称")
    location: Optional[str] = Field(default=None, description="地点")

    def __repr__(self):
        return f"<Site(id={self.id}, name={self.name}, location={self.location})>"


class Schedule(SQLModel, table=True):
    """
    组手赛程表
    """
    id: Optional[int] = Field(default=None, primary_key=True, description="唯一标识符")
    name: str = Field(default="", description="赛程名称")
    site_id: Optional[int] = Field(default=None, description="场地ID")
    red_id: Optional[int] = Field(default=None, description="红方选手ID")
    cyan_id: Optional[int] = Field(default=None, description="青方选手ID")
    status: Optional[int] = Field(default=0, description="比赛状态")  # todo Enum
    red_score: Optional[int] = Field(default=0, description="红方得分")
    red_foul: Optional[int] = Field(default=0, description="红方犯规次数")
    cyan_score: Optional[int] = Field(default=0, description="青方得分")
    cyan_foul: Optional[int] = Field(default=0, description="青方犯规次数")
    video_path: Optional[str] = Field(default=None, description="视频保存地址")
    winner_id: Optional[int] = Field(default=None, description="获胜方ID")
    preempt_id: Optional[int] = Field(default=0, description="先取ID")
    group: Optional[int] = Field(default=0, description="组别")

    def __repr__(self):
        return (f"<Schedule(id={self.id}, name={self.name}, site_id={self.site_id}, "
                f"red_id={self.red_id}, cyan_id={self.cyan_id}, status={self.status}, "
                f"red_score={self.red_score}, red_foul={self.red_foul}, cyan_score={self.cyan_score}, "
                f"cyan_foul={self.cyan_foul}, video_path={self.video_path}, winner_id={self.winner_id}, "
                f"preempt_id={self.preempt_id}, group={self.group})>")


class Athlete(SQLModel, table=True):
    """
    运动员个人信息
    """
    id: Optional[int] = Field(default=None, primary_key=True, description="唯一标识符")
    name: str = Field(default="", description="运动员名称")
    unit: str = Field(default="", description="单位名称")
    group: int = Field(default=0, description="组别")
    status: int = Field(default=0, description="运动员状态")  # todo enum
    place: int = Field(default=0, description="运动员名次，-1表示淘汰")

    def __repr__(self):
        return (f"<Athlete(id={self.id}, name={self.name}, unit={self.unit}, "
                f"group={self.group}, status={self.status}, place={self.place})>")


class ResponseModel(SQLModel, Generic[T]):
    """
    通用响应模型，用于标准化 API 响应格式
    """
    status: bool = Field(default=True, description="请求是否成功")
    code: int = Field(default=200, description="状态码")
    data: Optional[T] = Field(default=None, description="响应数据")
    message: str = Field(default="成功", description="描述信息")

    def __repr__(self):
        return (f"<ResponseModel(status={self.status}, code={self.code}, "
                f"data={self.data}, message={self.message})>")
