from rich.console import Console
from rich.prompt import Prompt
from .backup_manager import BackupManager

class BackupMenu:
    def __init__(self):
        self.console = Console()
        self.backup_manager = BackupManager()
    
    def show_menu(self):
        self.console.clear()
        self.console.print("\n=== Система Бэкапа ===", style="bold white")
        self.console.print("1. Запустить бэкап сейчас", style="green")
        self.console.print("2. Включить автобэкап (каждые 24ч)", style="blue")
        self.console.print("3. Настроить автобэкап", style="yellow")

    def run(self):
        while True:
            self.show_menu()
            choice = Prompt.ask("Выберите действие", choices=["1", "2", "3"])
            
            if choice == "1":
                self.console.print("\nЗапуск бэкапа...", style="blue")
                self.backup_manager.run()
            elif choice == "2":
                self.console.print("\nВключение автобэкапа...", style="blue")
                self.backup_manager.start_scheduled_backup()
            elif choice == "3":
                self.console.print("\nНастройка расписания автобэкапа...", style="yellow")
                self.backup_manager.configure_schedule()
