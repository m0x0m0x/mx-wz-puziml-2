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
    def calc(num1, num2, operation):
        if operation == "Add":
            return num1 + num2
        elif operation == "Subtract":
            return num1 - num2
        elif operation == "Multiply":
            return num1 * num2
        elif operation == "Divide":
            return num1 / num2 if num2 != 0 else "Error: Division by zero"

    calc_inter = gr.Interface(
        fn=calc,
        inputs=[
            gr.Number(label="Number 1"),
            gr.Number(label="Number 2"),
            gr.Radio(["Add", "Subtract", "Multiply", "Divide"], label="Operation"),
        ],
        outputs=gr.Number(label="Result"),  # Updated output format
        title="Simple Calculator",
        description="Perform basic arithmetic operations.",
    )

    calc_inter.launch()


# --- Random Jokes
def ran_jokes():
    header1("Random Jokes")

    def get_joke(message, history):
        jokes = [
            "Why did the scarecrow win an award? Because he was outstanding in his field.",
            "What do you call a fish wearing a crown? A king fish.",
            "Why don't scientists trust atoms? Because they make up everything.",
            "What do you get when you cross a snowman with a vampire? Frostbite.",
        ]
        return random.choice(jokes)

    demo = gr.ChatInterface(
        get_joke,
        type="messages",
        title="Chat with Random Response Generator",
    )

    demo.launch()
