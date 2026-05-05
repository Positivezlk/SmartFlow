from fastapi import APIRouter

from src.modules.notifications.service import NotificationService

router = APIRouter()
service = NotificationService()


@router.post('/test')
def test_notification(payload: dict):
    return service.send_test(payload)


@router.get('/settings')
def settings():
    return service.get_settings()
