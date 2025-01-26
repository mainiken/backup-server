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
██████╗  █████╗  ██████╗██╗  ██╗██╗   ██╗██████╗ 
██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██║   ██║██╔══██╗
██████╔╝███████║██║     █████╔╝ ██║   ██║██████╔╝
██╔══██╗██╔══██║██║     ██╔═██╗ ██║   ██║██╔═══╝ 
██████╔╝██║  ██║╚██████╗██║  ██╗╚██████╔╝██║     
╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     
"""
        # Печатаем ASCII art белым цветом
        self.console.print(backup_art, style="bold white")
        
        # Печатаем подпись
        self.console.print("\nby @mainecrypto", style="bold cyan")
        
        # Печатаем главное меню
        self.console.print("\n1. 🚀 Управление бэкапом", style="green")
        self.console.print("2. ⚙️  Настроить расписание", style="green")
        self.console.print("3. ❌ Выход", style="red")

    def show_backup_submenu(self):
        self.console.clear()
        self.console.print("\n=== Управление бэкапом ===", style="bold white")
        self.console.print("1. 📅 Запустить по расписанию", style="green")
        self.console.print("2. ▶️  Запустить сейчас", style="green")
        self.console.print("3. ↩️  Назад", style="yellow")
        
        choice = Prompt.ask("Выберите действие", choices=["1", "2", "3"])
        
        if choice == "1":
            self.backup_manager.run_scheduled()
        elif choice == "2":
            self.backup_manager.run()
        # choice == "3" просто вернёт в главное меню

    def run(self):
        """Основной цикл меню"""
        while True:
            self.show_menu()
            choice = Prompt.ask("Выберите действие", choices=["1", "2", "3"])
            
            if choice == "1":
                self.show_backup_submenu()
            elif choice == "2":
                self.backup_manager.configure_schedule()
            elif choice == "3":
                self.console.print("\nСпасибо за использование! by @mainecrypto", 
                                 style="bold cyan")
                break
