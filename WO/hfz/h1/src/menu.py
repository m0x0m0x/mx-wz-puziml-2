# Menu option to chose your models and work
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from .w1 import qwen15, llam2
import os

# Initialize the Rich console
console = Console()


def display_menu():
    # Define menu options
    options = [
        "1. deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
        "2. meta-llama/Llama-3.2-1B-Instruct",
        "3. Exit",
    ]

    # Create a fancy panel for the menu
    menu_text = "\n".join(options)
    console.print(
        Panel.fit(
            menu_text,
            title="Choose Model to Query",
            title_align="left",
            border_style="green",
        )
    )

    # Get user input
    choice = Prompt.ask("Enter your choice", choices=["1", "2", "3"], default="3")
    return int(choice)


def show_menu():
    os.system("clear")
    choice = display_menu()
    if choice == 1:
        qwen15()
    elif choice == 2:
        llam2()
    elif choice == 3:
        console.print("[bold red]Exiting...")
