# Building a chatbot interface using gradio

import gradio as gr
import random
from .utilz import header1
from rich.traceback import install

install(show_locals=True)

# -- random Response Generator


def ran_res():
    header1("Random Response Generator")

    def get_response(input_text):
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
