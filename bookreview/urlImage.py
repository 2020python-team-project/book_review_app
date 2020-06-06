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


if __name__ == "__main__":
    window = Tk()
    window.geometry("500x500+500+200")

    # # openapi로 이미지 url을 가져옴.
    # url = "http://tong.visitkorea.or.kr/cms/resource/74/2396274_image2_1.JPG"
    # with urllib.request.urlopen(url) as u:
    #     raw_data = u.read()
    #
    # im = Image.open(BytesIO(raw_data))

    url_image = UrlImage("https://bookthumb-phinf.pstatic.net/cover/157/688/15768821.jpg?type=m1&udate=20200111")
    image = url_image.get_image()

    Label(window, image=image, height=400, width=400).pack()

    window.mainloop()

