from tkinter import*
from io import BytesIO
import urllib.request
import urllib.error
from PIL import Image, ImageTk


class UrlImage:
    image = None

    def __init__(self, url):
        req = urllib.request.Request(url)
        try:
            with urllib.request.urlopen(req) as u:
                self.image = ImageTk.PhotoImage(Image.open(BytesIO(u.read())))
        except urllib.error.URLError as e:
            self.image = ImageTk.PhotoImage(file="Resource/Image/NoImage.png")
            print(e.reason)

    def get_image(self):
        return self.image

