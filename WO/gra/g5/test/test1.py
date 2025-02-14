import gradio as gr


def greet(name, intensity):
    return "Fuck, " + name + "Smell Pussy Ass" + "!" * int(intensity)


demo = gr.Interface(
    title="Booty Smell",
    description="Panty Smell Wamts",
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)

demo.launch()
