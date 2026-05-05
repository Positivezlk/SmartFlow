from fastapi import APIRouter

from src.modules.auth.router import router as auth_router
from src.modules.categories.router import router as categories_router
from src.modules.dashboard.router import router as dashboard_router
from src.modules.notifications.router import router as notifications_router
from src.modules.tasks.router import router as tasks_router
from src.modules.voice.router import router as voice_router

api_router = APIRouter()
api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_router.include_router(tasks_router, prefix="/tasks", tags=["tasks"])
api_router.include_router(categories_router, prefix="/categories", tags=["categories"])
api_router.include_router(dashboard_router, prefix="/dashboard", tags=["dashboard"])
api_router.include_router(voice_router, prefix="/voice", tags=["voice"])
api_router.include_router(notifications_router, prefix="/notifications", tags=["notifications"])
