# Tutorial Function all in here
import gradio as gr
from rich.traceback import install

install(show_locals=True)


# -- Greeter Function
def f1_greeter(name, intensity):
    return "Hello, " + name + "!<<>>>" * int(intensity)


def f1_greeter_launch(function=f1_greeter):
    f1l = gr.Interface(
        title="Gringo Booty Dancee",
        description="This is a one bad niggaz That is the main yaya ",
        fn=function,
        inputs=["text", "slider"],
        outputs=["text"],
    )
    f1l.launch()
