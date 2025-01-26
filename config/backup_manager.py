from .settings import settings
from .utils import setup_logger, TelegramNotifier
import tarfile
from datetime import datetime
import os
from pathlib import Path
import fnmatch

class BackupManager:
    def __init__(self):
        self.settings = settings
        self.logger = setup_logger()
        self.telegram = TelegramNotifier(settings.telegram_token, settings.chat_id)
        self.start_time = None
        self.end_time = None
        self.file_count = 0
        
    def should_exclude(self, path):
        """Проверяет, должен ли путь быть исключен из бэкапа"""
        for pattern in self.settings.exclude_dirs:
            if pattern.startswith('/'):
                if str(path).startswith(pattern):
                    return True
            else:
                if fnmatch.fnmatch(str(path), pattern) or \
                   any(fnmatch.fnmatch(part, pattern) for part in Path(path).parts):
                    return True
        return False

def create_backup(self):
    self.start_time = datetime.now()
    self.logger.info(f"Начало бэкапа: {self.start_time}")
    
    # Путь к директории, которую нужно бэкапить
    backup_source = os.getenv('BACKUP_SOURCE', '/home/your_username')  # Добавьте в .env
    
    # Создаем директорию для бэкапов если её нет
    self.settings.backup_dir.mkdir(parents=True, exist_ok=True)
    
    # Формируем имя файла бэкапа
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    backup_file = self.settings.backup_dir / f"backup_{timestamp}.tar.gz"
    
    try:
        with tarfile.open(backup_file, "w:gz") as tar:
            # Бэкапим только указанную директорию
            tar.add(backup_source, arcname=os.path.basename(backup_source))
            self.file_count += 1
            
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
        return backup_file
            
    except Exception as e:
        self.logger.error(f"Ошибка создания бэкапа: {e}")
        return None

    def _get_file_size(self, file_path):
        """Возвращает размер файла в человекочитаемом формате"""
        size_bytes = os.path.getsize(file_path)
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024:
                return f"{size_bytes:.2f}{unit}"
            size_bytes /= 1024
        return f"{size_bytes:.2f}TB"

    def run(self):
        try:
            backup_file = self.create_backup()
            if backup_file:
                self.telegram.send_file(backup_file)
                self.cleanup_old_backups()
                self.logger.info("Бэкап успешно создан и отправлен")
        except Exception as e:
            self.logger.error(f"Ошибка при создании бэкапа: {e}")
            
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
        except Exception as e:
            self.logger.error(f"Ошибка при очистке старых бэкапов: {e}")
            
    def configure_schedule(self):
        """Настройка расписания бэкапов"""
        try:
            from crontab import CronTab
            
            cron = CronTab(user=True)
            
            # Очищаем существующие задачи для этого скрипта
            cron.remove_all(comment='backup_script')
            
            # Получаем путь к текущему скрипту
            script_path = Path(__file__).parent.parent / 'main.py'
            
            # Создаем новую задачу
            job = cron.new(command=f'python3 {script_path} --run',
                          comment='backup_script')
            
            # Запрашиваем расписание
            schedule = input("""Выберите расписание:
1. Ежедневно
2. Еженедельно
3. Ежемесячно
Ваш выбор (1-3): """)
            
            if schedule == "1":
                hour = input("Введите час (0-23): ")
                job.setall(f'0 {hour} * * *')
            elif schedule == "2":
                day = input("Введите день недели (0-6, где 0 = воскресенье): ")
                hour = input("Введите час (0-23): ")
                job.setall(f'0 {hour} * * {day}')
            elif schedule == "3":
                day = input("Введите день месяца (1-31): ")
                hour = input("Введите час (0-23): ")
                job.setall(f'0 {hour} {day} * *')
            
            cron.write()
            self.logger.info("Расписание успешно настроено")
            
        except Exception as e:
            self.logger.error(f"Ошибка при настройке расписания: {e}")
