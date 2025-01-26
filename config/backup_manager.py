from .settings import settings
from .utils import setup_logger, TelegramNotifier
import tarfile
from datetime import datetime
import os
from pathlib import Path
import fnmatch
from rich.console import Console

class BackupManager:
    def __init__(self):
        self.settings = settings
        self.logger = setup_logger()
        self.telegram = TelegramNotifier(settings.telegram_token, settings.chat_id)
        self.console = Console()
        self.start_time = None
        self.end_time = None
        self.file_count = 0
        
        # Стандартные исключения
        self.default_excludes = [
            '*venv*',
            '*virtualenv*',
            '*.pyc',
            '__pycache__',
            '.git',
            'node_modules',
            '.env',
            '*.log',
            '*.tmp',
            '*.temp',
            '.idea',
            '.vscode',
            '*.swp',
            '*.swo',
            '.DS_Store',
            'Thumbs.db'
        ]

    def should_exclude(self, path):
        """Проверяет, должен ли путь быть исключен из бэкапа"""
        path_str = str(path)
        
        # Проверяем стандартные исключения
        for pattern in self.default_excludes:
            if fnmatch.fnmatch(path_str, pattern) or \
               any(fnmatch.fnmatch(part, pattern) for part in Path(path_str).parts):
                return True
                
        # Проверяем дополнительные исключения из настроек
        if hasattr(self.settings, 'additional_excludes'):
            for pattern in self.settings.additional_excludes:
                if fnmatch.fnmatch(path_str, pattern) or \
                   any(fnmatch.fnmatch(part, pattern) for part in Path(path_str).parts):
                    return True
                    
        return False

    def _get_file_size(self, file_path):
        """Возвращает размер файла в человекочитаемом формате"""
        size_bytes = os.path.getsize(file_path)
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024:
                return f"{size_bytes:.2f}{unit}"
            size_bytes /= 1024
        return f"{size_bytes:.2f}TB"

    def create_backup(self):
        """Создает резервную копию"""
        self.start_time = datetime.now()
        self.logger.info(f"Начало бэкапа: {self.start_time}")
        
        if not self.settings.backup_source:
            self.logger.error("Не указан BACKUP_SOURCE в .env файле")
            self.console.print("❌ Ошибка: не указан путь источника в .env файле", style="red")
            return None
        
        # Создаем директорию для бэкапов если её нет
        self.settings.backup_dir.mkdir(parents=True, exist_ok=True)
        
        # Формируем имя файла бэкапа
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        backup_file = self.settings.backup_dir / f"backup_{timestamp}.tar.gz"
        
        try:
            self.console.print(f"📂 Создание бэкапа из: {self.settings.backup_source}", style="yellow")
            with tarfile.open(backup_file, "w:gz") as tar:
                # Рекурсивно добавляем файлы, пропуская исключения
                for root, dirs, files in os.walk(self.settings.backup_source):
                    # Фильтруем директории
                    dirs[:] = [d for d in dirs if not self.should_exclude(os.path.join(root, d))]
                    
                    for file in files:
                        file_path = os.path.join(root, file)
                        if not self.should_exclude(file_path):
                            try:
                                tar.add(file_path, 
                                      arcname=os.path.relpath(file_path, 
                                                            str(self.settings.backup_source)))
                                self.file_count += 1
                                if self.file_count % 100 == 0:
                                    self.console.print(f"📊 Обработано файлов: {self.file_count}", 
                                                     style="blue")
                            except Exception as e:
                                self.logger.error(f"Ошибка при добавлении {file_path}: {e}")
                
            self.end_time = datetime.now()
            duration = self.end_time - self.start_time
            
            # Формируем отчет
            report = (
                f"📦 Бэкап завершён\n"
                f"📝 Файл: {backup_file.name}\n"
                f"📊 Размер: {self._get_file_size(backup_file)}\n"
                f"🕒 Начало: {self.start_time}\n"
                f"🕕 Окончание: {self.end_time}\n"
                f"⏱ Длительность: {duration}\n"
                f"📑 Обработано файлов: {self.file_count}"
            )
            
            self.logger.info(report)
            self.console.print(report, style="green")
            return backup_file
                
        except Exception as e:
            self.logger.error(f"Ошибка создания бэкапа: {e}")
            self.console.print(f"❌ Ошибка создания бэкапа: {e}", style="red")
            return None

    def cleanup_old_backups(self):
        """Удаляет старые бэкапы, оставляя только последние n штук"""
        try:
            backups = sorted(
                self.settings.backup_dir.glob("backup_*.tar.gz"),
                key=lambda x: x.stat().st_mtime,
                reverse=True
            )
            
            # Удаляем старые бэкапы
            for backup in backups[self.settings.keep_backups:]:
                backup.unlink()
                self.logger.info(f"Удален старый бэкап: {backup.name}")
                self.console.print(f"🗑️ Удален старый бэкап: {backup.name}", style="yellow")
        except Exception as e:
            self.logger.error(f"Ошибка при очистке старых бэкапов: {e}")

    def run(self):
        """Запускает процесс создания бэкапа"""
        try:
            self.console.print("🚀 Запуск процесса бэкапа...", style="blue")
            backup_file = self.create_backup()
            
            if backup_file:
                self.console.print("📤 Отправка файла в Telegram...", style="blue")
                self.telegram.send_file(backup_file)
                self.cleanup_old_backups()
                self.console.print("✅ Процесс бэкапа успешно завершен!", style="green")
            else:
                self.console.print("❌ Не удалось создать бэкап", style="red")
                
        except Exception as e:
            self.logger.error(f"Ошибка при выполнении бэкапа: {e}")
            self.console.print(f"❌ Ошибка при выполнении бэкапа: {
