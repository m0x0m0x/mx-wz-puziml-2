# tu3 - Making a QR Code Converter
import gradio as gr
import qrcode
from PIL import Image
from .utilz import header1
from rich.traceback import install

install(show_locals=True)


def gen_qr():
    header1("QR Code Generator")

    def make_qr(data):
        qr = qrcode.QRCode(
            version=2,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img = img.convert("RGBA")
        return img

    demo = gr.Interface(
        fn=make_qr,
        inputs="text",
        outputs="image",
        title="QR Code Generator",
        description="Generate QR Codes",
    )

    demo.launch()
