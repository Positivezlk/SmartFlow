class VoiceService:
    def parse_command(self, payload: dict) -> dict:
        text = payload.get('command_text', '').lower()
        if 'create task' in text:
            intent = 'create_task'
        elif 'today' in text:
            intent = 'tasks_today'
        elif 'completed' in text:
            intent = 'complete_task'
        else:
            intent = 'unknown'
        return {'intent': intent, 'command_text': text}

    def process(self, payload: dict) -> dict:
        parsed = self.parse_command(payload)
        return {'status': 'processed', 'parsed': parsed, 'message': 'Command processed'}

    """Mock voice service. Extension point for STT, AI parser and TTS."""

    def parse_command(self, payload: dict) -> dict:
        return {'status': 'mock', 'input': payload, 'intent': 'create_task'}

    def process(self, payload: dict) -> dict:
        return {'status': 'mock', 'result': 'Голосовая команда обработана (mock)', 'payload': payload}
