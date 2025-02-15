# Work1.py

from .ut import header1
import os
from rich.traceback import install
from dotenv import load_dotenv, dotenv_values
from rich import print as rprint

install(show_locals=True)

load_dotenv("src/.env")


# *******************************
# File Main function
def w1_main():
    header1("PrintSmellPantyKeys")
    brint_env()


# *******************************


def brint_env():
    # Loadin the env from .env
    header1("PrintSmellPantyKeys")
    geyz = dotenv_values("src/.env")
    for key, value in geyz.keys():
        rprint(f"{key}={value}")
