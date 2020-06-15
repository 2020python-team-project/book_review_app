from tkinter import *
from tkinter import font
from urlImage import UrlImage


class RecordDetailGUI:
    frame = None
    position = ()

    image_label = None
    book_image = None       # 지역으로 선언하면 인스턴스를 삭제하기 때문에 멤버로 가지고 있어야 함
    title_label = None
    author_label = None
    publisher_label = None
    pubdate_label = None
    price_label = None
    date_label = None
    comment_label = None
    rating_label = None

    back_button = None

    book = None

    def __init__(self, frame, x, y):
        self.frame = Frame(frame, width=420, height=460, bd=1, relief="solid", bg="white")
        self.position = (x, y)

        self.create_widget()
        self.place_widget()

    def create_widget(self):
        self.image_label = Label(self.frame)
        self.title_label = Label(self.frame)
        self.author_label = Label(self.frame)
        self.publisher_label = Label(self.frame)

        self.back_button = Button(self.frame, text="닫기", command=self.frame.place_forget)

    def place_widget(self):
        self.image_label.place(x=10, y=10)
        self.title_label.place(x=120, y=10)
        self.author_label.place(x=120, y=30)
        self.publisher_label.place(x=120, y=50)

        self.back_button.place(x=380, y=10)

    def open(self, book):
        self.book_image = UrlImage(book.image).get_image()

        self.image_label.configure(image=self.book_image)
        self.frame.place(x=self.position[0], y=self.position[1], anchor="n")
