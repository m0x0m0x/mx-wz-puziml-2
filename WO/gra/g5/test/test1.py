import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown("![](https://i.ibb.co/SX6n05rS/l.png)")
    gr.Markdown("<img src="https://i.ibb.co/SX6n05rS/l.png">")
    gr.Markdown("<h1><center>Open Explorer</center></h1>")

demo.launch()
