# Main work here
import os
from huggingface_hub import InferenceClient
from rich import print as rprint
from rich import inspect
from dotenv import load_dotenv

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

    client = InferenceClient(
        "meta-llama/Llama-3.3-70B-Instruct",
        token=os.getenv("HFA"),
    )
    cLient_reply = client.text_generation("Today is a great day")
    rprint(cLient_reply)
    inspect(cLient_reply)
