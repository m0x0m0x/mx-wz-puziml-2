import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown(
        "<div align='center'><img src='https://i.ibb.co/SX6n05rS/l.png' width='200'></div>"
    )
    gr.Markdown("<h1><center>Open Explorer</center></h1>")
    gr.Markdown("This is a test <br> Direct Hot reload <br> And Notty with he main")

    prompt = gr.Textbox(
        label="Smell Panty Pussy SnifFStink",
        type="text",
        placeholder="Smell Panty Pussy SnifFStink",
    )
    token = gr.Textbox(
        "HF Token",
        type="password",
        placeholder="Enter your HF Token",
        lines=1,
        max_lines=1,
    )

demo.launch()
