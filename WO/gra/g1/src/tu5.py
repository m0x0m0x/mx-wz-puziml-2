# Tabbed Interface
import gradio as gr
from .utilz import header1
from dotenv import load_dotenv
from rich.traceback import install

load_dotenv("src/.env")

install(show_locals=True)
