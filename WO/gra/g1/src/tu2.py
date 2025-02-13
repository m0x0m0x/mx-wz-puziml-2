# Work for tutorial 2 - Masterer Gradio Interface in 2025 Easier thatn you think
import gradio as gr
from rich.traceback import install

install(show_locals=True)


def f1_greet():
    def greet(name):
        if not name:  # Handles empty input
            return "Lick ninas pussy 😏"
        return f"Lick {name} pussy 😜"

    demo = gr.Interface(
        fn=greet,
        inputs="text",
        outputs="text",
        title="Booty Smellz",
        description="LickSniffing",
    )

    demo.launch()
