class NotificationService:
    """Mock notification service with extension points for email/push/ws/telegram."""

    def send_test(self, payload: dict) -> dict:
        return {'status': 'queued-mock', 'channel': payload.get('channel', 'websocket')}

    def get_settings(self) -> dict:
        return {'email': False, 'browser_push': False, 'telegram': False, 'websocket': True}
