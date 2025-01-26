from rich.console import Console
from rich.prompt import Prompt
from .backup_manager import BackupManager
from .settings import settings

class BackupMenu:
    def __init__(self):
        self.console = Console()
        self.backup_manager = BackupManager()
    
    def show_menu(self):
        self.console.clear()
        ascii_art = """
        
 ▄▄▄▄    ▄▄▄       ▄████▄   ██ ▄█▀ █    ██  ██▓███  
▓█████▄ ▒████▄    ▒██▀ ▀█   ██▄█▒  ██  ▓██▒▓██░  ██▒
▒██▒ ▄██▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▓██  ▒██░▓██░ ██▓▒
▒██░█▀  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▓▓█  ░██░▒██▄█▓▒ ▒
░▓█  ▀█▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄▒▒█████▓ ▒██▒ ░  ░
░▒▓███▀▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░
▒░▒   ░   ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░░░▒░ ░ ░ ░▒ ░     
 ░    ░   ░   ▒   ░        ░ ░░ ░  ░░░ ░ ░ ░░       
 ░            ░  ░░ ░      ░  ░      ░              
      ░           ░                                 

        """
        self.console.print(ascii_art, style="bold cyan")
        self.console.print("\nby @mainecrypto", style="bold blue")
        self.console.print(f"\nВремя бэкапа: {settings.backup_time}", style="yellow")
        self.console.print(f"Интервал: {settings.backup_interval} часов\n", style="yellow")
        self.console.print("1. 🚀 Запустить бэкап сейчас", style="green")
        self.console.print("2. ⏰ Запустить по расписанию", style="blue")

    def run(self):
        while True:
            self.show_menu()
            choice = Prompt.ask("Выберите действие", choices=["1", "2"])
            
            if choice == "1":
                self.backup_manager.run()
            elif choice == "2":
                self.backup_manager.start_scheduled_backup()
