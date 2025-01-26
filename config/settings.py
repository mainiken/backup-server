from dotenv import load_dotenv
import os
from pathlib import Path

class Settings:
    def __init__(self):
        load_dotenv()
        
        # Основные настройки
        self.telegram_token = os.getenv('TELEGRAM_TOKEN')
        self.chat_id = os.getenv('CHAT_ID')
        self.backup_dir = Path(os.getenv('BACKUP_DIR', '/root/backups'))
        self.keep_backups = int(os.getenv('KEEP_BACKUPS', 3))
        
        # Настройки логирования
        self.log_dir = Path('logs')
        self.log_file = self.log_dir / 'backup.log'
        
        # Список исключений
        self.exclude_dirs = [
            '/proc', '/sys', '/dev', '/run',
            '/media', '/mnt', '/tmp', str(self.backup_dir),
            '*venv*', '*.pyc', '__pycache__', '.git',
            'node_modules', '.idea', '.vscode'
        ]

settings = Settings()
