# Building a chatbot interface using gradio

import gradio as gr
import random
from .utilz import header1
from rich.traceback import install

install(show_locals=True)


# -- random Response Generator
def ran_res():
    header1("Random Response Generator")

    def get_response(message, history):
        responses = [
            "I am sorry, I don't understand.",
            "I am not sure I understand.",
            "I am not programmed to understand that.",
        ]
        return random.choice(responses)

    demo = gr.ChatInterface(
        get_response,
        type="messages",
        title="Chat with Random Response Generator",
    )

    demo.launch()


# -- Calculator Function


def kalk():
    header1("Simple Calculator")

    def calc(num1, num2, operation):
        if operation == "Add":
            return num1 + num2
        elif operation == "Subtract":
            return num1 - num2
        elif operation == "Multiply":
            return num1 * num2
        elif operation == "Divide":
            return num1 / num2

    calc_inter = gr.Interface(
        fn=calc,
        inputs=[
            gr.inputs.Number(label="Number 1"),
            gr.inputs.Number(label="Number 2"),
            gr.inputs.Radio(
                ["Add", "Subtract", "Multiply", "Divide"], label="Operation"
            ),
        ],
        outputs="number",
        title="Simple Calculator",
    )

    calc_inter.launch()
