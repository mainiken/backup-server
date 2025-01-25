import sys
from src.interface.cli import parse_args
from src.interface.menu import BackupMenu
from src.config.settings import settings
from src.utils.logger import setup_logger

def main():
    logger = setup_logger()
    
    if not settings.is_configured:
        logger.error("Application is not configured. Please check .env file.")
        sys.exit(1)
    
    args = parse_args()
    
    if args.run:
        # Запуск бэкапа напрямую (для cron)
        from src.backup.backup_manager import BackupManager
        backup_manager = BackupManager()
        backup_manager.run()
    else:
        # Запуск интерактивного меню
        menu = BackupMenu()
        menu.run()

if __name__ == "__main__":
    main()
