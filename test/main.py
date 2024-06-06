import pytest
from sqlmodel import create_engine, Session
from app.group_hands.model.models import *

# 创建测试数据库引擎
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, echo=True)

# 设置测试用例的 fixture
@pytest.fixture(name="session")
def session_fixture():
    # 创建数据库表
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    # 清除数据库表
    SQLModel.metadata.drop_all(engine)

def test_create_schedule(session: Session):
    # 创建新的 Schedule 实例
    schedule = Schedule(site_id=1, status=0, red_score=10, red_foul=1, cyan_score=15, cyan_foul=2)
    session.add(schedule)
    session.commit()
    session.refresh(schedule)

    # 验证 Schedule 实例是否正确保存
    assert schedule.id is not None
    assert schedule.site_id == 1
    assert schedule.status == 0
    assert schedule.red_score == 10
    assert schedule.red_foul == 1
    assert schedule.cyan_score == 15
    assert schedule.cyan_foul == 2

def test_read_schedule(session: Session):
    # 插入测试数据
    schedule = Schedule(site_id=2, status=1, red_score=20, red_foul=0, cyan_score=25, cyan_foul=1)
    session.add(schedule)
    session.commit()
    session.refresh(schedule)

    # 查询插入的数据
    queried_schedule = session.query(Schedule).filter(Schedule.id == schedule.id).first()

    # 验证查询结果
    assert queried_schedule is not None
    assert queried_schedule.site_id == 2
    assert queried_schedule.status == 1
    assert queried_schedule.red_score == 20
    assert queried_schedule.red_foul == 0
    assert queried_schedule.cyan_score == 25
    assert queried_schedule.cyan_foul == 1

def test_update_schedule(session: Session):
    # 插入测试数据
    schedule = Schedule(site_id=3, status=2, red_score=30, red_foul=2, cyan_score=35, cyan_foul=3)
    session.add(schedule)
    session.commit()
    session.refresh(schedule)

    # 更新 Schedule 实例
    schedule.status = 1
    schedule.red_score = 40
    session.commit()
    session.refresh(schedule)

    # 验证 Schedule 实例是否正确更新
    assert schedule.status == 1
    assert schedule.red_score == 40

def test_delete_schedule(session: Session):
    # 插入测试数据
    schedule = Schedule(site_id=4, status=0, red_score=50, red_foul=4, cyan_score=55, cyan_foul=5)
    session.add(schedule)
    session.commit()
    session.refresh(schedule)

    # 删除 Schedule 实例
    session.delete(schedule)
    session.commit()

    # 验证 Schedule 实例是否正确删除
    queried_schedule = session.query(Schedule).filter(Schedule.id == schedule.id).first()
    assert queried_schedule is None
