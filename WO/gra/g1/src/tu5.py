# Tabbed Interface
import gradio as gr
from .utilz import header1
from dotenv import load_dotenv
from rich.traceback import install
import math

load_dotenv("src/.env")

install(show_locals=True)

# --- Tabbed Interface ---


def kalk_tab():
    header1("Gradio Interface - Tabbed Calculator")

    # Basic Calculator
    def bas_cal(n1, op, n2):
        if op == "add":
            return n1 + n2
        elif op == "sub":
            return n1 - n2
        elif op == "mul":
            return n1 * n2
        elif op == "div":
            return n1 / n2

    # Scientific Calculator
    def sci_cal(n1, op):
        if op == "sin":
            return math.sin(n1)
        elif op == "cos":
            return math.cos(n1)
        elif op == "tan":
            return math.tan(n1)
        elif op == "log":
            return math.log(n1)
        elif op == "sqrt":
            return math.sqrt(n1)

    # Tabbed Interface
