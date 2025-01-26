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
            self.logger.info(f"Отправка сообщения в Telegram")
            response = requests.post(
                f'https://api.telegram.org/bot{self.token}/sendMessage',
                data={'chat_id': self.chat_id, 'text': text}
            )
            response.raise_for_status()
            self.logger.info("Сообщение успешно отправлено")
        except Exception as e:
            self.logger.error(f"Ошибка отправки сообщения: {str(e)}", exc_info=True)

    def send_file(self, file_path):
        try:
            self.logger.info(f"Начинаю отправку файла {file_path}")
            with open(file_path, 'rb') as file:
                self.logger.info("Файл открыт, отправляю в Telegram...")
                response = requests.post(
                    f'https://api.telegram.org/bot{self.token}/sendDocument',
                    data={'chat_id': self.chat_id},
                    files={'document': file}
                )
                self.logger.info(f"Ответ от Telegram: {response.status_code}")
                response.raise_for_status()
                self.logger.info("Файл успешно отправлен")
        except Exception as e:
            self.logger.error(f"Ошибка отправки файла: {str(e)}", exc_info=True)
