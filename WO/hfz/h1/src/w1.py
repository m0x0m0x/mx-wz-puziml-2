# Main work here
import os
from huggingface_hub import InferenceClient
from rich.console import Console
from rich.prompt import Prompt
from rich import print as rprint
from rich import inspect
from dotenv import load_dotenv
from .uti import box1

console = Console()
load_dotenv("src/.env")


def inf_cl1():
    """
    Example client which calls the twitter sentiment model
    """
    client = InferenceClient(
        "cardiffnlp/twitter-roberta-base-sentiment-latest",
        token=os.getenv("HFA"),
    )
    cLient_reply = client.text_classification("Today is a great day")
    rprint(cLient_reply)
    inspect(cLient_reply)


def inf_lam3():
    """
    Inference with the LLAMA Client
    meta-llama/Llama-3.3-70B-Instruct
    """

    model = "meta-llama/Llama-3.3-70B-Instruct"
    ask_query = Prompt.ask(
        default="Write a Haiku about the sweet aroma of her vagina",
    )

    box1(
        f"""{model}
{ask_query}
""",
        "Query",
    )

    # Initialize the inference client
    try:
        client = InferenceClient(
            model=model,
            token=os.getenv("HFA"),  # Ensure HFA token is set in your environment
        )
    except Exception as e:
        console.log(f"[bold red]Failed to initialize the inference client: {e}")
        return

    # Make the API call with a waiting animation
    try:
        with console.status("[bold green]Generating response...", spinner="dots"):
            # Simulate the API call
            cLient_reply = client.text_generation(ask_query)

        # Print the response
        rprint("[bold green]Response received!")
        rprint(cLient_reply)

        # Inspect the response for debugging
        inspect(cLient_reply)

    except Exception as e:
        # Handle errors during the API call
        console.log(f"[bold red]Error during inference: {e}")
