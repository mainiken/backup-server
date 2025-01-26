import logging
import requests
import os
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
            self.logger.error(f"Ошибка отправки сообщения: {str(e)}", exc_info=True)

    def send_file(self, file_path, caption=None):
        try:
            if not os.path.exists(file_path):
                self.logger.error(f"Файл не найден: {file_path}")
                return
                
            with open(file_path, 'rb') as file:
                data = {'chat_id': self.chat_id}
                if caption:
                    data['caption'] = caption
                    
                response = requests.post(
                    f'https://api.telegram.org/bot{self.token}/sendDocument',
                    data=data,
                    files={'document': file}
                )
                response.raise_for_status()
        except Exception as e:
            self.logger.error(f"Ошибка отправки файла: {str(e)}", exc_info=True)
