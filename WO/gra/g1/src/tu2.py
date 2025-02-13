# Work for tutorial 2 - Masterer Gradio Interface in 2025 Easier thatn you think
import gradio as gr
from .utilz import header1
from rich.traceback import install

install(show_locals=True)


# --- Basic Greeter Function ---
def f1_greet():
    header1("Gradio Interface - Basic Greeter Function")

    def greet(name):
        return f"Lick {name if name else 'unknown'} pussy 😜"

    demo = gr.Interface(
        fn=greet,
        inputs="text",
        outputs="text",
        title="Booty Smellz",
        description="LickSniffing",
    )

    demo.launch()


# --- String Reversal Fnction ---
def f2_rev_string():
    header1("Gradio Interface - String Reversal Function")

    def rev_string(s):
        return s[::-1]

    demo = gr.Interface(
        fn=rev_string,
        inputs="text",
        outputs="text",
        title="String Reversal",
        description="Reverse a string",
    )

    demo.launch()


# -- Classifier Example
def f3_cl_img():
    header1("Gradio Interface - Image Classifier DUMMY")

    def classify_image(img):
        return {
            "cat": 0.8,
            "dog": 0.1,
            "fish": 0.05,
            "horse": 0.03,
            "human": 0.02,
        }

    demo = gr.Interface(
        title="Bogus Image Classifier",
        description="This is a dummy image classifier",
        fn=classify_image,
        inputs="image",
        outputs="label",
    )

    demo.launch()


# --- Sentiment Analysis ---
def f4_sent():
    header1("Gradio Interface - Sentiment Analysis")

    def sentiment_analysis(text):
        return "Positive" if "good" in text else "Negative"

    demo = gr.Interface(
        fn=sentiment_analysis,
        inputs="text",
        outputs="text",
        title="Sentiment Analysis",
        description="Classify text as positive or negative",
    )

    demo.launch()


# -- Temeprature Converter ---
def f5_tmpc():
    header1("Gradio Interface - Temperature Converter")

    # Writing a seperate function that eill be called in the main function
    def far_to_cel(f):
        return (f - 32) * 5.0 / 9.0

    def fahrenheit_to_celsius(f):
        far_to_cel(f)

    demo = gr.Interface(
        fn=fahrenheit_to_celsius,
        inputs="number",
        outputs="number",
        title="Fahrenheit to Celsius",
        description="Convert Fahrenheit to Celsius",
    )

    demo.launch()
