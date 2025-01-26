from rich.console import Console
from rich.prompt import Prompt
from .backup_manager import BackupManager
import time

class BackupMenu:
    def __init__(self):
        self.console = Console()
        self.backup_manager = BackupManager()
    
    def animated_rainbow_print(self, text, duration=1):
        """Печатает текст с анимированным радужным эффектом"""
        colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
        lines = text.splitlines()
        start_time = time.time()
        
        while time.time() - start_time < duration:
            self.console.clear()
            colors = colors[1:] + [colors[0]] 
            
            for i, line in enumerate(lines):
                if line.strip():
                    color = colors[i % len(colors)]
                    self.console.print(line, style=f"bold {color}")
                else:
                    self.console.print(line)
            
            time.sleep(0.1)
        
        self.console.clear()
        for i, line in enumerate(lines):
            if line.strip():
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
        
