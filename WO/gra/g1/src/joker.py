# This is for getting jokes from -
# https://github.com/benjhar/JokeAPI-Python#readme
# Code has been merged from src/tu4.py

import gradio as gr
import random
import asyncio
from jokeapi import Jokes  # Import JokeAPI
from rich.traceback import install

install(show_locals=True)


def jokerz():
    def fetch_joke():
        """Fetch a random joke from JokeAPI synchronously."""

        async def get_joke():
            j = await Jokes()  # Initialize the class
            joke = await j.get_joke()  # Retrieve a random joke
            return (
                joke["joke"]
                if joke["type"] == "single"
                else f"{joke['setup']} - {joke['delivery']}"
            )

        return asyncio.run(get_joke())  # Run the async function synchronously

    def ran_jokes():
        def get_joke(message, history):
            return fetch_joke()  # Fetch a real joke dynamically

        demo = gr.ChatInterface(
            get_joke,
            type="messages",
            title="Chat with a Random Joke Generator 🤣",
            description="Chat and get random jokes from JokeAPI!",
        )

        demo.launch()

    ran_jokes()  # Run the function
