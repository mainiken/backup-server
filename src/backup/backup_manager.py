from ..config.settings import settings
from ..utils.logger import setup_logger
from ..utils.telegram import TelegramClient
import tarfile
from pathlib import Path
import logging

class BackupManager:
    def __init__(self):
        self.settings = settings
        self.logger = setup_logger()
        self.telegram = TelegramClient(settings.telegram_token, settings.chat_id)
        # ... остальной код класса ...
