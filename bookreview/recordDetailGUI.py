from tkinter import *
from tkinter import font
from tkinter import messagebox
from urlImage import UrlImage
import rating_image
from Cmodule.dateString import *

TEXT_START = 1.0
TEXT_END = END


class RecordDetailGUI:
    frame = None
    position = ()
    default_font = None
    title_font = None
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

    edit_image = None
    remove_image = None
    edit_button = None
    remove_button = None
    back_button = None

    remove_message_box = None

    record_gui = None
    book = None

    def __init__(self, frame, x, y):
        self.frame = Frame(frame, width=420, height=460, bd=1, relief="solid", bg="white")
        self.position = (x, y)
        self.set_font()

        self.set_widget()
        self.place_widget()

    def set_font(self):
        self.default_font = font.Font(family="메이플스토리", weight="bold", size=12)
        self.title_font = font.Font(family="메이플스토리", weight="bold", size=14)
        self.text_font = font.Font(family="메이플스토리", weight="bold", size=13)
        self.date_font = font.Font(family="메이플스토리", weight="bold", size=16)

    def set_widget(self):
        self.image_label = Label(self.frame, bg="white", bd=1, relief="solid")
        self.title_label = Label(self.frame, bg="white", font=self.title_font, anchor="w", justify="left", wraplength=300)
        self.author_label = Label(self.frame, bg="white", font=self.default_font)
        self.publisher_label = Label(self.frame, bg="white", font=self.default_font)
        self.pubdate_label = Label(self.frame, bg="white", font=self.default_font)
        self.price_label = Label(self.frame, bg="white", font=self.default_font)

        self.date_label = Label(self.frame, bg="white", font=self.date_font)
        self.rating_label = Label(self.frame, bg="white")

        self.comment_frame = Frame(self.frame)
        self.comment_text = Text(self.comment_frame, font=self.text_font, width=34, height=8, relief="solid",
                                 cursor="arrow")
        self.comment_scrollbar = Scrollbar(self.comment_frame)
        self.comment_text["yscrollcommand"] = self.comment_scrollbar.set
        self.comment_scrollbar["command"] = self.comment_text.yview


        self.edit_image = PhotoImage(file="Resource/Image/edit.png")
        self.edit_button = Button(self.frame, image=self.edit_image)
        self.remove_image = PhotoImage(file="Resource/Image/remove.png")
        self.remove_button = Button(self.frame, image=self.remove_image, command=self.show_remove_message)
        self.back_button = Button(self.frame, text="닫기", font=self.default_font,
                                  command=self.frame.place_forget)

    def show_remove_message(self):
        ok = messagebox.askokcancel("삭제", "삭제한 데이터는 복구할 수 없습니다.\n진짜로 삭제하시겠습니까?")
        if ok:
            self.record_gui.book_manager.remove_book(self.book)
            self.frame.place_forget()

    def place_widget(self):
        self.image_label.place(x=10, y=15)

        self.title_label.place(x=120, y=15)
        self.author_label.place(x=120, y=60)
        self.publisher_label.place(x=120, y=80)
        self.pubdate_label.place(x=120, y=100)
        self.price_label.place(x=120, y=120)

        self.date_label.place(x=10, y=170)
        self.rating_label.place(x=250, y=150)

        self.comment_text.pack(side="left")
        self.comment_scrollbar.pack(side="right", fill="y")
        self.comment_frame.place(x=210, y=200, anchor="n")

        self.edit_button.place(x=10, y=400)
        self.remove_button.place(x=80, y=400)
        self.back_button.place(x=410, y=430, anchor="e")

    def open(self, book):
        self.book = book
        self.book_image = UrlImage(book.image).get_image()
        self.image_label.configure(image=self.book_image)

        self.title_label.configure(text=book.title)
        self.author_label.configure(text=book.author)
        self.publisher_label.configure(text=book.publisher)
        self.pubdate_label.configure(text=f"출판일: {book.pubdate}")
        self.price_label.configure(text=f"가격: {book.price}")

        self.rating_label.configure(image=rating_image.get_rating_image(book.rating))

        # date_str = book.edit_date[:4] + '.' + book.edit_date[4:6] + '.' + book.edit_date[6:]
        self.date_label.configure(text=get_dot_format(book.edit_date))

        self.comment_text.configure(state="normal")
        self.comment_text.delete(TEXT_START, TEXT_END)
        self.comment_text.insert(TEXT_START, book.user_comment)
        self.comment_text.configure(state="disable")

        self.frame.place(x=self.position[0], y=self.position[1], anchor="n")

    def set_record_gui(self, gui):
        self.record_gui = gui

