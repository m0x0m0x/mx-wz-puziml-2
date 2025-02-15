# Work1.py

from .ut import header1
import os
from rich.traceback import install
from dotenv import load_dotenv
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
    for key, value in os.environ.items():
        rprint(f"{key}={value}")
