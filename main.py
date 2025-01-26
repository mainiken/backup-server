from config.menu import BackupMenu
from config.settings import settings
import sys

def main():
    if not all([settings.telegram_token, settings.chat_id]):
        print("Ошибка: проверьте настройки в файле .env")
        sys.exit(1)
        
    menu = BackupMenu()
    menu.run()

if __name__ == "__main__":
    main()
