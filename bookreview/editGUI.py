# 책을 서재에 담기 전, 책의 정보를 수정하는 Frame과 UI
from tkinter import *
from tkinter import font
from urlImage import *
import copy
from urlImage import UrlImage

TEXT_START = 1.0
TEXT_END = END


class EditGUI:
    position = None
    frame = None

    date_gui = None

    image_label = None
    title_label = None
    author_label = None
    publisher_label = None

    close_button = None
    save_button = None

    rating_scale = None

    comment_edit_frame = None
    comment_edit_text = None
    comment_edit_scrollbar = None

    book = None

    # 책 리스트
    book_manager = None

    def __init__(self, frame, x, y):
        self.position = (x, y)
        self.default_font = font.Font(size=11, weight='bold', family='메이플스토리')

        self.frame = Frame(frame, bg="white", width=420, height=460)

        # for debug
        self.frame.configure(bd=3, relief="solid")

        self.create_widget()
        self.set_widget()
        self.place_widget()

    def create_widget(self):
        self.image_label = Label(self.frame)
        self.title_label = Label(self.frame)
        self.author_label = Label(self.frame)
        self.publisher_label = Label(self.frame)

        self.rating_scale = Scale(self.frame)

        self.save_button = Button(self.frame)
        self.close_button = Button(self.frame)

        # 날짜 입력 위젯
        self.date_gui = DateEditGUI(self.frame)

        self.comment_edit_frame = Frame(self.frame)
        self.comment_edit_text = Text(self.comment_edit_frame)
        self.comment_edit_scrollbar = Scrollbar(self.comment_edit_frame)

    def set_widget(self):
        self.image_label.configure(bg="white", bd=1, relief="solid")
        self.title_label.configure(bg="white", font=self.default_font)
        self.author_label.configure(bg="white", font=self.default_font)
        self.publisher_label.configure(bg="white", font=self.default_font)

        self.save_button.configure(text="저장", font=self.default_font, command=self.save)
        self.close_button.configure(text="닫기", font=self.default_font, command=self.close)

        self.rating_scale.configure(command=self.select, orient="horizontal",
                                    showvalue=False, tickinterval=1, from_=1, to=5, length=130,
                                    bg="white", label="별점", width=20, bd=0, relief="solid",
                                    sliderlength=20, sliderrelief="solid", troughcolor="gold",
                                    font=self.default_font, activebackground="gold")

        self.comment_edit_text.configure(font=self.default_font, width=34, height=10, relief="solid")

        self.date_gui.set()

        # Text 객체와 Scrollbar 객체의 연결
        self.comment_edit_text["yscrollcommand"] = self.comment_edit_scrollbar.set
        self.comment_edit_scrollbar["command"] = self.comment_edit_text.yview

    def place_widget(self):
        self.image_label.place(x=25, y=70)
        self.title_label.place(x=120, y=80)
        self.author_label.place(x=120, y=105)
        self.publisher_label.place(x=120, y=130)

        self.save_button.place(x=300, y=20)
        self.close_button.place(x=350, y=20)

        self.rating_scale.place(x=250, y=180)

        self.date_gui.place(25, 220)

        self.comment_edit_text.pack(side="left")
        self.comment_edit_scrollbar.pack(side="right", fill="y")
        self.comment_edit_frame.place(x=25, y=260)

    def open(self, book, image):
        self.book = copy.copy(book)
        self.image_label["image"] = image
        self.title_label.configure(text=self.book.title)
        self.author_label.configure(text=self.book.author)
        self.publisher_label.configure(text=self.book.publisher)

        self.frame.place(x=self.position[0], y=self.position[1], anchor="n")
        self.frame.tkraise()

    def close(self):
        self.frame.place_forget()

    def save(self):
        self.book.user_comment = self.comment_edit_text.get(TEXT_START, TEXT_END)
        self.book.edit_date = self.date_gui.get()
        self.book.rating = self.rating_scale.get()
        self.book_manager.add_book(self.book)

        self.close()

    def debug(self):
        # self.frame.place(x=self.position[0], y=self.position[1], anchor="n")
        # self.frame.tkraise()
        # print(self.date_gui.get())
        pass

    def select(self, event):
        pass

    def link(self, book_manager):
        self.book_manager = book_manager


class DateEditGUI:
    frame = None
    font = None

    label = None
    year_spinbox = None
    month_spinbox = None
    date_spinbox = None

    def __init__(self, frame):
        self.frame = Frame(frame)
        self.font = font.Font(size=14, weight='bold', family='메이플스토리')

        self.label = Label(self.frame)
        self.year_spinbox = Spinbox(self.frame)
        self.month_spinbox = Spinbox(self.frame)
        self.date_spinbox = Spinbox(self.frame)

    def set(self):
        self.label.configure(font=self.font, text="날짜: ", bg="white")
        self.year_spinbox.configure(font=self.font, relief="solid", width=4, from_=2000, to=2100)
        self.month_spinbox.configure(font=self.font, relief="solid", width=2, from_=1, to=12)
        self.date_spinbox.configure(font=self.font, relief="solid", width=2, from_=1, to=31)

    def place(self, x, y):
        self.label.pack(side="left")
        self.year_spinbox.pack(side="left")
        self.month_spinbox.pack(side="left")
        self.date_spinbox.pack(side="left")
        self.frame.place(x=x, y=y)

    def get(self):
        return f"{self.year_spinbox.get()}" \
               f"{self.month_spinbox.get().zfill(2)}" \
               f"{self.date_spinbox.get().zfill(2)}"
