from src.t1 import create_interface

# Create the Gradio instance at module level
run_create_interface = create_interface()
demo = run_create_interface


def main():
    demo.launch()


if __name__ == "__main__":
    main()
