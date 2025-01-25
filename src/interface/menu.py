from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from ..backup.backup_manager import BackupManager
from ..config.settings import settings

class BackupMenu:
    def __init__(self):
        self.console = Console()
        self.backup_manager = BackupManager()
    
    def show_main_menu(self):
        self.console.clear()
        self.console.print(Panel.fit(
            "[bold blue]Система резервного копирования[/bold blue]\n\n"
            "1. 🚀 Запустить бэкап\n"
            "2. ⚙️  Настроить расписание\n"
            "3. 📊 Показать статистику\n"
            "4. ❌ Выход"
        ))
    
    def run(self):
        while True:
            self.show_main_menu()
            choice = Prompt.ask("Выберите действие", choices=["1", "2", "3", "4"])
            
            if choice == "1":
                self.backup_manager.run()
            elif choice == "2":
                self.backup_manager.configure_backup_schedule()
            elif choice == "3":
                self.show_statistics()
            elif choice == "4":
                break
