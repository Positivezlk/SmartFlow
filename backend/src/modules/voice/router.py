from fastapi import APIRouter

from src.modules.voice.service import VoiceService

router = APIRouter()
service = VoiceService()


@router.post('/command')
def command(payload: dict):
    return service.parse_command(payload)


@router.post('/process')
def process(payload: dict):
    return service.process(payload)
