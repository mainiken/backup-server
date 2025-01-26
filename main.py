from config.menu import BackupMenu
from config.settings import settings
from config.backup_manager import BackupManager
import sys
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Backup System')
    parser.add_argument('--a', type=int, choices=[1, 2],
                      help='1: Backup now, 2: Start scheduled backup')
    return parser.parse_args()

def main():
    if not all([settings.telegram_token, settings.chat_id]):
        print("Ошибка: проверьте настройки в файле .env")
        sys.exit(1)

    args = parse_args()
    backup_manager = BackupManager()
    
    if args.a:
        if args.a == 1:
            backup_manager.run()
        elif args.a == 2:
            backup_manager.start_scheduled_backup()
        sys.exit(0)
    
    menu = BackupMenu()
    menu.run()

if __name__ == "__main__":
    main()
