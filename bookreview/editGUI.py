# 책을 서재에 담기 전, 책의 정보를 수정하는 Frame과 UI
from tkinter import *
from tkinter import font
import time
from urlImage import *
from book import Book
import rating_image
import Sounds

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

    rating_label = None
    rating = int()
    default_image = None
    good_image = None
    normal_image = None
    bad_image = None

    comment_edit_frame = None
    comment_edit_text = None
    comment_edit_scrollbar = None

    book_dic = None

    # 책 리스트
    book_manager = None

    def __init__(self, frame, x, y):
        self.position = (x, y)
        self.default_font = font.Font(size=11, weight='bold', family='메이플스토리')
        self.title_font = font.Font(size=13, weight='bold', family='메이플스토리')

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

        self.rating_label = Label(self.frame)

        self.save_button = Button(self.frame)
        self.close_button = Button(self.frame)

        # 날짜 입력 위젯
        self.date_gui = DateEditGUI(self.frame)

        self.comment_edit_frame = Frame(self.frame)
        self.comment_edit_text = Text(self.comment_edit_frame)
        self.comment_edit_scrollbar = Scrollbar(self.comment_edit_frame)

    def set_widget(self):
        self.image_label.configure(bg="white", bd=1, relief="solid")
        self.title_label.configure(bg="white", font=self.title_font, anchor="w",
                                   justify="left", wraplength=270)
        self.author_label.configure(bg="white", font=self.default_font)
        self.publisher_label.configure(bg="white", font=self.default_font)

        self.save_button.configure(text="저장", font=self.default_font, command=self.save)
        self.close_button.configure(text="닫기", font=self.default_font, command=self.close)

        self.date_gui.set()
        self.rating_label.configure(bg="white")
        self.rating_label.bind("<Button-1>", self.set_rating)

        self.comment_edit_text.configure(font=self.default_font, width=34, height=10, relief="solid")

        # Text 객체와 Scrollbar 객체의 연결
        self.comment_edit_text["yscrollcommand"] = self.comment_edit_scrollbar.set
        self.comment_edit_scrollbar["command"] = self.comment_edit_text.yview

    def place_widget(self):
        self.image_label.place(x=25, y=60)
        self.title_label.place(x=120, y=60)
        self.author_label.place(x=120, y=130)
        self.publisher_label.place(x=120, y=150)

        self.save_button.place(x=300, y=20)
        self.close_button.place(x=350, y=20)

        self.rating_label.place(x=370, y=200, anchor="e")
        self.date_gui.place(370, 240)

        self.comment_edit_text.pack(side="left")
        self.comment_edit_scrollbar.pack(side="right", fill="y")
        self.comment_edit_frame.place(x=25, y=260)

    def start_edit(self, book, image):
        self.book_dic = book    # 복사할 필요 없..지?
        self.image_label.configure(image=image)
        self.title_label.configure(text=self.book_dic["title"])
        self.author_label.configure(text=self.book_dic["author"])
        self.publisher_label.configure(text=self.book_dic["publisher"])

        self.rating = 0
        self.rating_label.configure(image=rating_image.default)
        self.date_gui.reset()

        self.comment_edit_text.delete(TEXT_START, TEXT_END)

        self.frame.place(x=self.position[0], y=self.position[1], anchor="n")
        self.frame.tkraise()

    def close(self):
        self.frame.place_forget()

    def save(self):
        book = Book(
            title=self.book_dic["title"],
            link=self.book_dic["link"],
            image=self.book_dic["image"],
            author=self.book_dic["author"],
            price=self.book_dic["price"],
            publisher=self.book_dic["publisher"],
            pubdate=self.book_dic["pubdate"],
            description=self.book_dic["description"],
            comment=self.comment_edit_text.get(TEXT_START, TEXT_END),
            date=self.date_gui.get(),
            rating=self.rating
        )
        self.book_manager.add_book(book)
        self.close()
        Sounds.띠딩()

    def debug(self):
        # self.frame.place(x=self.position[0], y=self.position[1], anchor="n")
        # self.frame.tkraise()
        # print(self.date_gui.get())
        pass

    def set_rating(self, event):
        x = event.x
        # 0~39 123~211 246~334
        if x < 39:
            self.rating = 1
            self.rating_label.configure(image=rating_image.bad)
        elif 55 < x < 94:
            self.rating = 2
            self.rating_label.configure(image=rating_image.normal)
        elif 110 < x < 334:
            self.rating = 3
            self.rating_label.configure(image=rating_image.good)

    def link(self, book_manager):
        self.book_manager = book_manager


class DateEditGUI:
    frame = None
    font = None

    label = None
    year_spinbox = None
    month_spinbox = None
    date_spinbox = None

    year = None
    month = None
    day = None

    def __init__(self, frame):
        self.frame = Frame(frame)
        self.font = font.Font(size=14, weight='bold', family='메이플스토리')

        self.label = Label(self.frame)
        self.year_spinbox = Spinbox(self.frame)
        self.month_spinbox = Spinbox(self.frame)
        self.date_spinbox = Spinbox(self.frame)

    def set(self):
        self.year = IntVar(self.frame)
        self.month = IntVar(self.frame)
        self.day = IntVar(self.frame)

        self.reset()

        self.label.configure(font=self.font, text="날짜: ", bg="white")
        self.year_spinbox.configure(font=self.font, relief="solid", width=4, from_=2000, to=2100, state="readonly",
                                    cursor="arrow", textvariable=self.year)
        self.month_spinbox.configure(font=self.font, relief="solid", width=2, from_=1, to=12, state="readonly",
                                     cursor="arrow", textvariable=self.month)
        self.date_spinbox.configure(font=self.font, relief="solid", width=2, from_=1, to=31, state="readonly",
                                    cursor="arrow", textvariable=self.day)

    def place(self, x, y):
        self.label.pack(side="left")
        self.year_spinbox.pack(side="left")
        self.month_spinbox.pack(side="left")
        self.date_spinbox.pack(side="left")
        self.frame.place(x=x, y=y, anchor="e")

    def get(self):
        return f"{self.year_spinbox.get()}" \
               f"{self.month_spinbox.get().zfill(2)}" \
               f"{self.date_spinbox.get().zfill(2)}"

    def reset(self):
        local_time = time.localtime(time.time())
        self.year.set(local_time.tm_year)
        self.month.set(local_time.tm_mon)
        self.day.set(local_time.tm_mday)
