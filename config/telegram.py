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
    def send_file(self, file_path):
        try:
            self.logger.info(f"Начинаю отправку файла {file_path}")
            
            # Проверяем существование файла
            if not os.path.exists(file_path):
                self.logger.error(f"Файл не найден: {file_path}")
                return
                
            with open(file_path, 'rb') as file:
                self.logger.info("Файл открыт, отправляю в Telegram...")
                
                # Добавляем caption для различения файлов
                caption = "Backup file" if str(file_path).endswith('.tar.gz') else "Log file"
                
                response = requests.post(
                    f'https://api.telegram.org/bot{self.token}/sendDocument',
                    data={
                        'chat_id': self.chat_id,
                        'caption': caption
                    },
                    files={'document': file}
                )
                self.logger.info(f"Ответ от Telegram: {response.status_code}")
                response.raise_for_status()
                self.logger.info("Файл успешно отправлен")
        except Exception as e:
            self.logger.error(f"Ошибка отправки файла: {str(e)}", exc_info=True)
