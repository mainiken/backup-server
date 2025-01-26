from config.menu import BackupMenu
from config.settings import settings
from config.backup_manager import BackupManager
import sys
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Система резервного копирования')
    parser.add_argument('--run', action='store_true', help='Запустить бэкап напрямую (для cron)')
    return parser.parse_args()

def main():
    # Проверяем настройки
    if not all([settings.telegram_token, settings.chat_id]):
        print("Ошибка: проверьте настройки в файле .env")
        sys.exit(1)
    
    args = parse_args()
    
    if args.run:
        # Режим прямого запуска (для cron)
        backup_manager = BackupManager()
        backup_manager.run()
    else:
        # Интерактивный режим
        menu = BackupMenu()
        menu.run()

if __name__ == "__main__":
    main()
