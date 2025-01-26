from dotenv import load_dotenv
import os
from pathlib import Path

class Settings:
    def __init__(self):
        load_dotenv()
        self.telegram_token = os.getenv('TELEGRAM_TOKEN')
        self.chat_id = os.getenv('CHAT_ID')
        self.backup_dir = Path(os.getenv('BACKUP_DIR', '/root/backups'))
        self.backup_source = os.getenv('BACKUP_SOURCE')
        self.keep_backups = int(os.getenv('KEEP_BACKUPS', 3))
        self.log_dir = Path('logs')
        self.log_file = self.log_dir / 'backup.log'
        self.exclude_dirs = [
            '/proc', '/sys', '/dev', '/run',
            '/media', '/mnt', '/tmp', str(self.backup_dir),
            '*venv*', '*.pyc', '__pycache__', '.git',
            'node_modules', '.idea', '.vscode'
        ]

settings = Settings()
