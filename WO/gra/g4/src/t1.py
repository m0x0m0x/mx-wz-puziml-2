# Mastering Blocks in Gradio 2025 Ultimate Guide

import gradio as gr
from .utilz import hea1, hea2
from rich.traceback import install
from rich import print as rprint

install(show_locals=True)


# ****** Main Function Runner ******


def t1_main_runner():
    func_events()


# ************************************

# -- Example 1  - Greeter Function---


def func_greet():
    hea1("Hello Pussy Lickers")

    def greet(name):
        return f" {name}! Smell her Pussy "

    with gr.Blocks() as demo:
        gr.Markdown("# Welcome Panty Smeller")

        with gr.Row():
            inp = gr.Textbox(label="Entery Mistress name")
            out = gr.Textbox(label="Panty Smell")

        with gr.Column():
            btn = gr.Button("Panty Smell")
            gr.Markdown("Panty Smell add beloww")

        btn.click(greet, inputs=inp, outputs=out)

    demo.launch()


# -- Example 2 - Blocks and Events  ---


def func_events():
    hea2("Events and Blocks")

    def process_text(text):
        return rprint(f"[green]Processed: {text.upper()}[/green]")

    with gr.Blocks() as demo:
        gr.Markdown("# Text Processing Demo")

        with gr.Box():
            inp = gr.Textbox(label="Enter Text", placeholder="Bastard Type Here")
            out = gr.Textbox(label="Processed Text", value="", interactive=False)

        btn = gr.Button("rape..")
        btn.click(process_text, inputs=inp, outputs=out)

        inp.change(process_text, inputs=inp, outputs=out)

    demo.launch()
