# Work1.py

from .ut import header1
from rich.traceback import install
from dotenv import load_dotenv

install(show_locals=True)

load_dotenv("src/.env")


# File Main function
def w1_main():
    header1("Hello World")
