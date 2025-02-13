# Tutorial Function all in here
import gradio as gr
from rich.traceback import install

install(show_locals=True)


# -- Greeter Function
def f1_greeter(name, intensity):
    return "Hello, " + name + "!<<>>>" * int(intensity)


def f1_greeter_launch(function=f1_greeter):
    f1l = gr.Interface(
        title="""Gringo Booty Dancee
        This is the second line of the title
        And this is the third line""",
        description="This is a one bad niggaz That is the main yaya ",
        fn=function,
        inputs=["text", "slider"],
        outputs=["text"],
    )
    f1l.launch()


# --- f2 = Multiply Funcion --
def f2_mul_launch():
    # --- Sub-function: Multiply ---
    def f2_mul(n1, n2):
        return n1 * n2

    # --- Gradio Interface ---
    f2mul = gr.Interface(
        fn=f2_mul,
        inputs=[gr.Number(label="Number1"), gr.Number(label="Number2")],
        outputs=gr.Textbox(label="Result"),
        title="MuliPussy",
        description="Where do you go",
    )

    f2mul.launch()
