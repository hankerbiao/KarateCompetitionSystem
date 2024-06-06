from fastapi import APIRouter, HTTPException
from core.db import SessionDep
from app.group_hands.model.models import MatchScore, Schedule
from sqlalchemy.exc import SQLAlchemyError
from fastapi import Query
from core.enum import ColorEnum, MatchUpdateType

router = APIRouter()


# 定义枚举类


@router.put("/match/update", response_model=MatchScore)
def update_match(
        db: SessionDep,
        match_score: MatchScore,
        update_type: MatchUpdateType = Query(...),
):
    """
    更新指定ID的比赛成绩记录或犯规记录
    """
    try:
        # 获取要更新的记录
        existing_match = db.get(Schedule, match_score.schedule_id)
        if not existing_match:
            raise HTTPException(status_code=404, detail="Match score not found")

        # 更新记录属性
        if update_type == MatchUpdateType.score:
            if match_score.color == ColorEnum.RED:
                current_score = existing_match.red_score
                existing_match.red_score = current_score + 1
            else:
                current_score = existing_match.cyan_score
                existing_match.cyan_score = current_score + 1
        elif update_type == MatchUpdateType.foul:
            if match_score.color == ColorEnum.RED:
                current_score = existing_match.red_foul
                existing_match.red_foul = current_score + 1
            else:
                current_score = existing_match.cyan_foul
                existing_match.cyan_foul = current_score + 1

        # 提交事务
        db.add(existing_match)
        db.commit()
        db.refresh(existing_match)

        return match_score
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error updating match record")
