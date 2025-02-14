# This wile will have the actual functions
import gradio as gr
from .utilz import hea1, hea2
from rich.traceback import install
from rich import print as rprint

install(show_locals=True)


# *** Main Function Caller ***
def g1_main_call():
    func1()


# ******************************


# --- Test Function 1 ---
def func1():
    hea2("Function 1")
