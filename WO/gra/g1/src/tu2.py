# Work for tutorial 2 - Masterer Gradio Interface in 2025 Easier thatn you think
import gradio as gr
from rich.traceback import install

install(show_locals=True)


def f1_greet():
    def greet(name="ina"):
        return f"Lick {name} pussy "

    demo = gr.Interface(fn=greet, inputs="text", outputs="text", title=[])

    demo.launch()
