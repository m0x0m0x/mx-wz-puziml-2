import gradio as gr
from src.t1 import func1


def main():
    demo = func1()
    demo.launch()


if __name__ == "__main__":
    main()
