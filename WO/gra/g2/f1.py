import marimo

__generated_with = "0.11.2"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
        #  Testing Gradio Work here
        - Lets see how gradio beahves in this env


        """
    )
    return


@app.cell
def _():
    import gradio as gr
    # -- Greeter Function
    def f1_greeter(name, intensity):
        return "Hello, " + name + "!<<>>>" * int(intensity)

    f1l = gr.Interface(
        title="""Gringo Booty Dancee
        This is the second line of the title
        And this is the third line""",
        description="This is a one bad niggaz That is the main yaya ",
        fn=f1_greeter,
        inputs=["text", "slider"],
        outputs=["text"],
            )
    f1l.launch()

    return f1_greeter, f1l, gr


@app.cell
def _(mo):
    mo.md(
        r"""
        # Important Note Gradio Has Trouble Spawning in Marimo 
        - cant use gradio with marimo inside your codespaces
        """
    )
    return


if __name__ == "__main__":
    app.run()
