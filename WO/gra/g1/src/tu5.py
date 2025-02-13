# Tabbed Interface
import gradio as gr
from .utilz import header1
from dotenv import load_dotenv
from rich.traceback import install

load_dotenv("src/.env")

install(show_locals=True)

# --- Tabbed Interface ---


def bas_cal(n1, op, n2):
    if op == "add":
        return n1 + n2
    elif op == "sub":
        return
