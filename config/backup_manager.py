from .settings import settings
from .telegram import TelegramNotifier
import tarfile
from datetime import datetime, timedelta  
import os
from pathlib import Path
import fnmatch
from rich.console import Console
import logging
import time
import signal

class BackupManager:
    def __init__(self):
        self.settings = settings
        self.logger = logging.getLogger(__name__)
        self.telegram = TelegramNotifier(settings.telegram_token, settings.chat_id)
        self.console = Console()
        self.start_time = None
        self.end_time = None
        self.file_count = 0
        self.running = True
        signal.signal(signal.SIGINT, self.handle_shutdown)
        signal.signal(signal.SIGTERM, self.handle_shutdown)

    def handle_shutdown(self, signum, frame):
        self.running = False
        self.console.print("\nОстановка процесса бэкапа...", style="yellow")
        
    def create_backup(self):
        self.file_count = 0  # Сброс счетчика для нового бэкапа
        self.start_time = datetime.now()
        self.logger.info(f"Начало бэкапа: {self.start_time}")
        
        if not self.settings.backup_source:
            self.logger.error("Не указан BACKUP_SOURCE в .env файле")
            self.console.print("❌ Ошибка: не указан путь источника в .env файле", style="red")
            return None
        
        self.settings.backup_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        backup_file = self.settings.backup_dir / f"backup_{timestamp}.tar.gz"
        
        try:
            self.console.print(f"📂 Создание бэкапа из: {self.settings.backup_source}", style="yellow")
            with tarfile.open(backup_file, "w:gz") as tar:
                for root, dirs, files in os.walk(self.settings.backup_source):
                    if not self.running:
                        raise InterruptedError("Процесс остановлен пользователем")
                    
                    # Фильтруем директории и файлы
                    dirs[:] = [d for d in dirs if not any(fnmatch.fnmatch(d, pattern) for pattern in self.settings.exclude_dirs)]
                    
                    for file in files:
                        file_path = os.path.join(root, file)
                        if not any(fnmatch.fnmatch(file_path, pattern) for pattern in self.settings.exclude_dirs):
                            try:
                                arcname = os.path.relpath(file_path, self.settings.backup_source)
                                tar.add(file_path, arcname=arcname)
                                self.file_count += 1
                                if self.file_count % 100 == 0:
                                    self.console.print(f"📊 Обработано файлов: {self.file_count}", style="blue")
                            except Exception as e:
                                self.logger.error(f"Ошибка при добавлении {file_path}: {e}")
            
            return backup_file
                
        except Exception as e:
            self.logger.error(f"Ошибка создания бэкапа: {e}")
            self.console.print(f"❌ Ошибка создания бэкапа: {e}", style="red")
            if backup_file.exists():
                backup_file.unlink()
            return None

    def _get_file_size(self, file_path):
        size_bytes = os.path.getsize(file_path)
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024:
                return f"{size_bytes:.2f}{unit}"
            size_bytes /= 1024
        return f"{size_bytes:.2f}TB"

    def cleanup_old_backups(self):
        try:
            backups = sorted(
                self.settings.backup_dir.glob("backup_*.tar.gz"),
                key=lambda x: x.stat().st_mtime,
                reverse=True
            )[self.settings.keep_backups:]
            
            for backup in backups:
                backup.unlink()
                self.logger.info(f"Удален старый бэкап: {backup.name}")
                self.console.print(f"🗑️ Удален старый бэкап: {backup.name}", style="yellow")
        except Exception as e:
            self.logger.error(f"Ошибка при очистке старых бэкапов: {e}")

    def start_scheduled_backup(self):
        self.running = True
        self.console.print(f"Запуск автоматического бэкапа каждые {self.settings.backup_interval} часов", style="blue")
        try:
            while self.running:
                now = datetime.now()
                backup_time = datetime.strptime(self.settings.backup_time, "%H:%M").time()
                next_backup = datetime.combine(now.date(), backup_time)
                
                if now.time() > backup_time:
                    next_backup = datetime.combine(now.date() + timedelta(days=1), backup_time)
                
                if now < next_backup:
                    wait_seconds = (next_backup - now).seconds
                    self.console.print(f"Следующий бэкап в {self.settings.backup_time}", style="blue")
                    time.sleep(wait_seconds)
                
                if self.running:
                    self.run()
                    time.sleep(self.settings.backup_interval * 3600)
                    
        except KeyboardInterrupt:
            self.running = False
            self.console.print("\nАвтобэкап остановлен", style="yellow")

    def run(self):
        try:
            self.console.print("🚀 Запуск процесса бэкапа...", style="blue")
            backup_file = self.create_backup()
            
            if backup_file:
                report = (
                    f"📝 Файл: {backup_file.name}\n"
                    f"📊 Размер: {self._get_file_size(backup_file)}\n"
                    f"📑 Обработано файлов: {self.file_count}"
                )
                
                self.console.print("📤 Отправка в Telegram...", style="blue")
                self.telegram.send_file(backup_file, caption=report)
                self.console.print("✅ Процесс бэкапа успешно завершен!", style="green")
                
                # Очистка после успешной отправки
                self.cleanup_old_backups()
            else:
                self.console.print("❌ Не удалось создать бэкап", style="red")
                
        except Exception as e:
            self.logger.error(f"Ошибка при выполнении бэкапа: {e}")
            self.console.print(f"❌ Ошибка при выполнении бэкапа: {e}", style="red")
