import logging
import requests
from pathlib import Path
from .settings import settings

def setup_logger():
    settings.log_dir.mkdir(exist_ok=True)
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(settings.log_file),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

class TelegramNotifier:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        self.logger = setup_logger()
        
    def send_message(self, text):
        try:
            response = requests.post(
                f'https://api.telegram.org/bot{self.token}/sendMessage',
                data={'chat_id': self.chat_id, 'text': text}
            )
            response.raise_for_status()
        except Exception as e:
            self.logger.error(f"Ошибка отправки сообщения в Telegram: {e}")

    def send_file(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                response = requests.post(
                    f'https://api.telegram.org/bot{self.token}/sendDocument',
                    data={'chat_id': self.chat_id},
                    files={'document': file}
                )
                response.raise_for_status()
        except Exception as e:
            self.logger.error(f"Ошибка отправки файла в Telegram: {e}")
