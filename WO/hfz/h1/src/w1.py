# Main work here
import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv("src/.env")


client.text_classification("Today is a great day")


def inf_cl1():
    client = InferenceClient(
        "cardiffnlp/twitter-roberta-base-sentiment-latest",
        token="hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    )
