# Building a chatbot interface using gradio

import gradio as gr
import random
import requests as rq
from .utilz import header1
from dotenv import load_dotenv
from rich.traceback import install

load_dotenv("src/.env")

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


# --- Counts number of works in a message ---
def count_words():
    def count_words(message, history):
        return f"Message contains {len(message.split())} words."

    demo = gr.ChatInterface(
        count_words,
        title="Count Words",
    )

    demo.launch()


# --- Getting Temparatures from a city ---
def get_temp():
    weather_data = {
        "London": "Cloudy, 10C",
        "New York": "Sunny, 18C",
        "Tokyo": "Rainy, 12C",
        "Paris": "Clear, 22C",
        "Berlin": "Windy, 5C",
        "Sydney": "Partly Cloudy, 25C",
        "Moscow": "Snowy, -2C",
        "Los Angeles": "Sunny, 20C",
        "Mumbai": "Humid, 30C",
        "Cape Town": "Breezy, 15C",
    }

    def get_temperature(message, history):
        city = message.capitalize()
        return weather_data.get(city, "City Not Found")

    temp_inter = gr.ChatInterface(
        get_temperature,
        title="Weather Bot",
    )

    temp_inter.launch()
