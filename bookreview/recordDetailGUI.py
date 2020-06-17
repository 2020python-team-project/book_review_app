from tkinter import *
from tkinter import font
from urlImage import UrlImage
import rating_image

TEXT_START = 1.0
TEXT_END = END


class RecordDetailGUI:
    frame = None
    position = ()
    default_font = None
    text_font = None
    date_font = None

    book_image = None       # 지역으로 선언하면 인스턴스를 삭제하기 때문에 멤버로 가지고 있어야 함
    image_label = None
    title_label = None
    author_label = None
    publisher_label = None
    pubdate_label = None
    price_label = None

    rating_image = None
    rating_label = None
    date_label = None

    comment_frame = None
    comment_text = None
    comment_scrollbar = None

    back_button = None

    book = None

    def __init__(self, frame, x, y):
        self.frame = Frame(frame, width=420, height=460, bd=1, relief="solid", bg="white")
        self.position = (x, y)
        self.set_font()

        self.set_widget()
        self.place_widget()

    def set_font(self):
        self.default_font = font.Font(family="메이플스토리", weight="bold", size=14)
        self.text_font = font.Font(family="메이플스토리", weight="bold", size=13)
        self.date_font = font.Font(family="메이플스토리", weight="bold", size=16)

    def set_widget(self):
        self.image_label = Label(self.frame, bg="white", bd=1, relief="solid")
        self.title_label = Label(self.frame, bg="white", font=self.default_font)
        self.author_label = Label(self.frame, bg="white", font=self.default_font)
        self.publisher_label = Label(self.frame, bg="white", font=self.default_font)
        self.pubdate_label = Label(self.frame, bg="white", font=self.default_font)
        self.price_label = Label(self.frame, bg="white", font=self.default_font)

        self.date_label = Label(self.frame, bg="white", font=self.date_font)
        self.rating_label = Label(self.frame, bg="white")

        self.comment_frame = Frame(self.frame)
        self.comment_text = Text(self.comment_frame, font=self.text_font, width=34, height=10, relief="solid",
                                 cursor="arrow")
        self.comment_scrollbar = Scrollbar(self.comment_frame)
        self.comment_text["yscrollcommand"] = self.comment_scrollbar.set
        self.comment_scrollbar["command"] = self.comment_text.yview

        self.back_button = Button(self.frame, text="닫기", font=self.default_font,
                                  command=self.frame.place_forget)

    def place_widget(self):
        self.image_label.place(x=10, y=15)

        self.title_label.place(x=120, y=15)
        self.author_label.place(x=120, y=40)
        self.publisher_label.place(x=120, y=65)
        self.pubdate_label.place(x=120, y=90)
        self.price_label.place(x=120, y=115)

        self.date_label.place(x=10, y=170)
        self.rating_label.place(x=250, y=150)

        self.comment_text.pack(side="left")
        self.comment_scrollbar.pack(side="right", fill="y")
        self.comment_frame.place(x=210, y=200, anchor="n")

        self.back_button.place(x=410, y=430, anchor="e")

    def open(self, book):
        self.book_image = UrlImage(book.image).get_image()
        self.image_label.configure(image=self.book_image)

        self.title_label.configure(text=book.title)
        self.author_label.configure(text=book.author)
        self.publisher_label.configure(text=book.publisher)
        self.pubdate_label.configure(text=f"출판일: {book.pubdate}")
        self.price_label.configure(text=f"가격: {book.price}")

        self.rating_label.configure(image=rating_image.get_rating_image(book.rating))
        date_str = book.edit_date[:4] + '.' + book.edit_date[4:6] + '.' + book.edit_date[6:]
        self.date_label.configure(text=date_str)

        self.comment_text.configure(state="normal")
        self.comment_text.delete(TEXT_START, TEXT_END)
        self.comment_text.insert(TEXT_START, book.user_comment)
        self.comment_text.configure(state="disable")

        self.frame.place(x=self.position[0], y=self.position[1], anchor="n")

