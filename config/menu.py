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

__/\\\\\\\\\\\\\_______/\\\\\\\\\___________/\\\\\\\\\__/\\\________/\\\__/\\\________/\\\__/\\\\\\\\\\\\\___        
 _\/\\\/////////\\\___/\\\\\\\\\\\\\______/\\\////////__\/\\\_____/\\\//__\/\\\_______\/\\\_\/\\\/////////\\\_       
  _\/\\\_______\/\\\__/\\\/////////\\\___/\\\/___________\/\\\__/\\\//_____\/\\\_______\/\\\_\/\\\_______\/\\\_      
   _\/\\\\\\\\\\\\\\__\/\\\_______\/\\\__/\\\_____________\/\\\\\\//\\\_____\/\\\_______\/\\\_\/\\\\\\\\\\\\\/__     
    _\/\\\/////////\\\_\/\\\\\\\\\\\\\\\_\/\\\_____________\/\\\//_\//\\\____\/\\\_______\/\\\_\/\\\/////////____    
     _\/\\\_______\/\\\_\/\\\/////////\\\_\//\\\____________\/\\\____\//\\\___\/\\\_______\/\\\_\/\\\_____________   
      _\/\\\_______\/\\\_\/\\\_______\/\\\__\///\\\__________\/\\\_____\//\\\__\//\\\______/\\\__\/\\\_____________  
       _\/\\\\\\\\\\\\\/__\/\\\_______\/\\\____\////\\\\\\\\\_\/\\\______\//\\\__\///\\\\\\\\\/___\/\\\_____________ 
        _\/////////////____\///________\///________\/////////__\///________\///_____\/////////_____\///______________

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
