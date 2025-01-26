from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from .backup_manager import BackupManager

class BackupMenu:
    def __init__(self):
        self.console = Console()
        self.backup_manager = BackupManager()
    
    def show_menu(self):
        self.console.print(Panel.fit(
            "1. 🚀 Запустить бэкап\n"
            "2. ⚙️  Настроить расписание\n"
            "3. ❌ Выход"
        ))
    
    def run(self):
        while True:
            self.show_menu()
            choice = Prompt.ask("Выберите действие", choices=["1", "2", "3"])
            if choice == "1":
                self.backup_manager.run()
            elif choice == "2":
                self.backup_manager.configure_schedule()
            elif choice == "3":
                break
