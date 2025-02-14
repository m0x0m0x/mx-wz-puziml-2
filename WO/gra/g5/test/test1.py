import gradio as gr


def greet(name, intensity):
    return "Fuck, " + name + "Smell Pussy" + "!" * int(intensity)


demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text", label="SmellPanty"],
)

demo.launch()
