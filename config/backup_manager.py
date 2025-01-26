from .settings import settings
from .utils import setup_logger, TelegramNotifier
import tarfile
from datetime import datetime
import os

class BackupManager:
    def __init__(self):
        self.settings = settings
        self.logger = setup_logger()
        self.telegram = TelegramNotifier(settings.telegram_token, settings.chat_id)
        self.start_time = None
        self.end_time = None
        self.file_count = 0
        
    def create_backup(self):
        self.start_time = datetime.now()
        self.logger.info(f"Начало бэкапа: {self.start_time}")
        
        # Код создания бэкапа...
        
    def run(self):
        try:
            backup_file = self.create_backup()
            if backup_file:
                self.telegram.send_file(backup_file)
                self.logger.info("Бэкап успешно создан и отправлен")
        except Exception as e:
            self.logger.error(f"Ошибка при создании бэкапа: {e}")
            
    def configure_schedule(self):
        # Код настройки расписания...
        pass
