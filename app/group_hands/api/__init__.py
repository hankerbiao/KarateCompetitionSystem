from fastapi import APIRouter

from app.group_hands.api.v1 import schedules, athlete, fields

api_route = APIRouter()

api_route.include_router(fields.router, tags=["场地信息"])
api_route.include_router(schedules.router, tags=["赛程信息"])
api_route.include_router(athlete.router, tags=["运动员信息"])
