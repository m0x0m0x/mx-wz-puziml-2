import gradio as gr
import asyncio
from .utilz import header1
from jokeapi import Jokes  # Import JokeAPI
from rich.traceback import install

install(show_locals=True)


def jokerz():
    header1("Get Random Jokes From API")
    """Main function containing all sub-functions for fetching and displaying jokes."""

    async def get_joke():
        """Fetch a random joke asynchronously from JokeAPI."""
        j = Jokes()  # ✅ Initialize normally (no await)
        joke = j.get_joke()  # ✅ Await only the actual API call

        if isinstance(joke, list):  # ❌ Prevent 'list can't be used in await'
            joke = joke[0]  # Take the first joke

        return (
            joke["joke"]
            if joke["type"] == "single"
            else f"{joke['setup']} - {joke['delivery']}"
        )

    def fetch_joke():
        """Handles sync & async cases without crashing."""
        try:
            return asyncio.run(get_joke())  # ✅ Convert async to sync safely
        except RuntimeError:
            # If an event loop is already running (e.g., inside Gradio), use `asyncio.create_task()`
            loop = asyncio.get_event_loop()
            return loop.run_until_complete(get_joke())

    def get_joke_response(message, history):
        """Handles incoming chat messages and returns a joke."""
        return fetch_joke()

    def run_interface():
        """Creates and returns the Gradio ChatInterface."""
        return gr.ChatInterface(
            get_joke_response,
            type="messages",
            title="Chat with a Random Joke Generator 🤣",
            description="Chat and get random jokes from JokeAPI!",
        )

    # ✅ Auto-launch inside this function
    demo = run_interface()
    demo.launch()  # ✅ LAUNCHES AUTOMATICALLY
