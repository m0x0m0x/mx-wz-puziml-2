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
    tabbed_inter = gr.TabbedInterface(
        tabs=[
            gr.Interface(
                fn=bas_cal,
                inputs=[
                    gr.Number(label="Number 1"),
                    gr.Radio(["add", "sub", "mul", "div"], label="Operation"),
                    gr.Number(label="Number 2"),
                ],
                outputs=gr.Number(label="Result"),
                title="Basic Calculator",
                description="Perform basic arithmetic operations.",
            ),
            gr.Interface(
                fn=sci_cal,
                inputs=[
                    gr.Number(label="Number 1"),
                    gr.Radio(["sin", "cos", "tan", "log", "sqrt"], label="Operation"),
                ],
                outputs=gr.Number(label="Result"),
                title="Scientific Calculator",
                description="Perform scientific operations.",
            ),
        ],
        title="Tabbed Calculator",
    )

    tabbed_inter.launch()
