# Main work here
import os
from huggingface_hub import InferenceClient
from rich.console import Console
from rich.prompt import Prompt
from rich import print as rprint
from rich import inspect
from dotenv import load_dotenv
from .uti import green_box, blue_box, l_error
from datetime import datetime

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
    os.system("clear")
    """
    Inference with the LLAMA Client
    meta-llama/Llama-3.3-70B-Instruct
    """

    console.rule("Inference with the LLAMA Client", style="blue")
    model = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
    ask_query = Prompt.ask(
        default="Write a Haiku about the sweet aroma of her vagina",
    )

    blue_box(
        f"""{model}
{ask_query}""",
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
        with console.status("[bold green]Generating response...\n", spinner="dots"):
            # Simulate the API call
            client_reply = client.text_generation(ask_query)

        # Print the response
        rprint("[bold green]Response received!")
        green_box(client_reply, "sucess")

        # Inspect the response for debugging
        inspect(client_reply)

        # Write the results to a text file with today's date and time appended to the name
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"rez/results_{timestamp}.txt"

        # Ensure the directory exists
        os.makedirs("rez", exist_ok=True)

        with open(filename, "w") as file:
            file.write(f"Model: {model}\n")
            file.write(f"Query: {ask_query}\n")
            file.write(f"Response: {client_reply}\n")

    except Exception as e:
        # Handle errors during the API call
        l_error(e)

    console.rule("END", style="blue")
