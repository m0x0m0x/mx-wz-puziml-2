# Adding main logic here and then called in app.py
import gradio as gr
from .utilz import hea1


def create_interface():
    hea1("This is a test")
    with gr.Blocks() as demo:
        gr.Markdown("<div align='center'><img src='l.png' width='200'></div>")
        gr.Markdown("<h1><center>Open Explorer</center></h1>")
        gr.Markdown("This is a test <br> Direct Hot reload <br> And Notty with he main")
        gr.Markdown(" # Bladnista")
        gr.Markdown(" > Booty Smeller")

        prompt = gr.Textbox(
            label="Smell Janda ",
            type="text",
            placeholder="Smell Panty Pussy SnifFStink",
        )
        token = gr.Textbox(
            label="HF Token",
            type="password",
            placeholder="Enter your HF Token",
        )

        with gr.Row():
            generate_bth = gr.Button("Generate", variant="primary")

    return demo
