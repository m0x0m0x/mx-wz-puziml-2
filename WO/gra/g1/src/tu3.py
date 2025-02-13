# tu3 - Making a QR Code Converter
import gradio as gr
import qrcode
from PIL import Image
from .utilz import header1
from rich.traceback import install

install(show_locals=True)
