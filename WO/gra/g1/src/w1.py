# Tutorial Function all in here
import gradio as gr
from rich.traceback import install

install(show_locals=True)


# -- Greeter Function
def f1_greeter(name, intensity):
    return "Hello, " + name + "!" * int(intensity)


def f1_greeter_launch(function=f1_greeter):
    iface = gr.Interface(
        fn=function,
        inputs=["text", "slider"],
        outputs=["text"],
    )
    iface.launch()
