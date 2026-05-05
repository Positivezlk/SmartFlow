class VoiceService:
    """Mock voice service. Extension point for STT, AI parser and TTS."""

    def parse_command(self, payload: dict) -> dict:
        return {'status': 'mock', 'input': payload, 'intent': 'create_task'}

    def process(self, payload: dict) -> dict:
        return {'status': 'mock', 'result': 'Голосовая команда обработана (mock)', 'payload': payload}
