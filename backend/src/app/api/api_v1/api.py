from fastapi import APIRouter

from app.api.api_v1.endpoints import users, login, courses, ping

api_router = APIRouter()
api_router.include_router(ping.router, tags=["Test"])
api_router.include_router(login.router, tags=["Login"])  
api_router.include_router(users.router, prefix="/users", tags=["Users"])  
api_router.include_router(courses.router, prefix="/courses", tags=["Courses"])
