# Work1.py

from .ut import header1, green_box
import os
from rich import print as rprint
from rich.traceback import install
from dotenv import load_dotenv, dotenv_values

install(show_locals=True)

load_dotenv("src/.env")


# *******************************
# File Main function
def w1_main():
    header1("PrintSmellPantyKeys")


# *******************************


# Function for printing the keys
def brint_env():
    # Loadin the env from .env
    header1("PrintSmellPantyKeys")
    geyz = dotenv_values("src/.env")
    for key, value in geyz.items():
        val = f"{key}={value}"
        green_box(val, "Keyz")


# Actual Transformer function
