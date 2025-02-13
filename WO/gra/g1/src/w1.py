# Tutorial Function all in here
import gradio as gr
from rich.traceback import install

install(show_locals=True)


# -- Greeter Function
def f1_greeter(name, intensity):
    return "Hello, " + name + "!" * int(intensity)


def f1_greeter_launch():
    iface = gr.Interface(
        fn=f1_greeter,
        inputs=[
            gr.inputs.Textbox(name="name"),
            gr.inputs.Slider(minimum=1, maximum=10, default=1, label="intensity"),
        ],
        outputs="text",
        title="Greeter",
        description="Say hello to someone!",
    )
    iface.launch()
