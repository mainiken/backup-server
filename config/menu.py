from rich.console import Console
from rich.prompt import Prompt
from .backup_manager import BackupManager

class BackupMenu:
    def __init__(self):
        self.console = Console()
        self.backup_manager = BackupManager()
    
    def show_menu(self):
        # ASCII art для BACKUP
        backup_art = """
 ▄▄▄▄    ▄▄▄       ▄████▄   ██ ▄█▀█    ██  ██▓███  
▓█████▄ ▒████▄    ▒██▀ ▀█   ██▄█▒ ██  ▓██▒▓██░  ██▒
▒██▒ ▄██▒██  ▀█▄  ▒▓█    ▄ ▓███▄░▓██  ▒██░▓██░ ██▓▒
▒██░█▀  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄▓▓█  ░██░▒██▄█▓▒ ▒
░▓█  ▀█▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄▒▒█████▓ ▒██▒ ░  ░
░▒▓███▀▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒▒▓▒ ▒ ▒ ▒▓▒░ ░  ░
▒░▒   ░   ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░░▒░ ░ ░ ░▒ ░     
 ░    ░   ░   ▒   ░        ░ ░░ ░ ░░░ ░ ░ ░░       
 ░            ░  ░░ ░      ░  ░     ░              
      ░          ░                                  
        """
        
        menu_text = f"""
{backup_art}

1. 🚀 Запустить бэкап
2. ⚙️  Настроить расписание
3. ❌ Выход

by @mainecrypto
"""
        self.console.print(menu_text)
    
    def run(self):
        while True:
            self.show_menu()
            choice = Prompt.ask("Выберите действие", choices=["1", "2", "3"])
            if choice == "1":
                self.backup_manager.run()
            elif choice == "2":
                self.backup_manager.configure_schedule()
            elif choice == "3":
                self.console.print("\nСпасибо за использование! by @mainecrypto")
                break
