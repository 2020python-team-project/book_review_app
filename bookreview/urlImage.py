from tkinter import*
from io import BytesIO
import urllib.request
from PIL import Image, ImageTk


class UrlImage:
    url = str()
    image = None

    def __init__(self, url):
        self.url = url
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()

        self.image = ImageTk.PhotoImage(Image.open(BytesIO(raw_data)))

    def get_image(self):
        return self.image
