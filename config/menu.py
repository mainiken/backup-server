from rich.console import Console
from rich.prompt import Prompt
from .backup_manager import BackupManager
import time

class BackupMenu:
    def __init__(self):
        self.console = Console()
        self.backup_manager = BackupManager()
    
    def rainbow_print(self, text):
        """Печатает текст, используя разные цвета для каждой строки"""
        colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
        lines = text.splitlines()
        for i, line in enumerate(lines):
            if line.strip():  # Пропускаем пустые строки
                color = colors[i % len(colors)]
                self.console.print(line, style=f"bold {color}")
            else:
                self.console.print(line)
    
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
        self.animated_rainbow_print(backup_art)
        
        self.console.print("\nby @mainecrypto", style="bold cyan")
        
        self.console.print("\n1. 🚀 Запустить бэкап", style="green")
        self.console.print("2. ⚙️  Настроить расписание", style="green")
        self.console.print("3. ❌ Выход", style="red")

    def run(self):
        """Основной цикл меню"""
        while True:
            self.show_menu()
            choice = Prompt.ask("Выберите действие", choices=["1", "2", "3"])
            
            if choice == "1":
                self.backup_manager.run()
            elif choice == "2":
                self.backup_manager.configure_schedule()
            elif choice == "3":
                self.console.print("\nСпасибо за использование! by @mainecrypto", 
                                 style="bold cyan")
                break
