class NotificationService:
    def __init__(self):
        self._settings = {'email': True, 'browser_push': True, 'telegram': False, 'websocket': True}

    def send_test(self, payload: dict) -> dict:
        return {'status': 'sent', 'channel': payload.get('channel', 'websocket'), 'message': payload.get('message', 'Test')}

    def get_settings(self) -> dict:
        return self._settings
