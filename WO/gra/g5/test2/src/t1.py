# Main Logic Here
import gradio as gr


def func1():
    with gr.Blocks() as demo:
        gr.Markdown(
            "<div align='center'><img src='https://i.ibb.co/SX6n05rS/l.png' width='200'></div>"
        )
        gr.Markdown("<h1><center>Open Explorer</center></h1>")
        gr.Markdown("This is a test <br> Direct Hot reload <br> And Notty with he main")

        prompt = gr.Textbox(
            label="Bootango - What is the main ",
            type="text",
            placeholder="WhatThis",
        )
        token = gr.Textbox(
            label="HF Token",
            type="password",
            placeholder="Enter your HF Token",
        )

        with gr.Row():
            generate_bth = gr.Button("Generate", variant="primary")

    return demo
