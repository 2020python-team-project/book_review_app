# 책을 서재에 담기 전, 책의 정보를 수정하는 Frame과 UI
from tkinter import *
from tkinter import font


class EditGUI:
    position = None
    frame = None
    comment_edit_frame = None

    image_label = None
    rating_scale = None
    close_button = None
    comment_edit_text = None
    comment_edit_scrollbar = None

    book = None

    def __init__(self, frame, x, y):
        self.position = (x, y)
        self.TempFont = font.Font(size=11, weight='bold', family='Consolas')

        self.frame = Frame(frame, bg="white", width=420, height=330)

        # for debug
        self.frame.configure(bd=3, relief="solid")

        self.create_widget()
        self.set_widget()
        self.place_widget()

        # self.frame.place(x=x, y=y, anchor="n")

    def create_widget(self):
        self.image_label = Label(self.frame)
        self.rating_scale = Scale(self.frame)
        self.close_button = Button(self.frame)

        self.comment_edit_frame = Frame(self.frame)
        self.comment_edit_text = Text(self.comment_edit_frame)
        self.comment_edit_scrollbar = Scrollbar(self.comment_edit_frame)

    def set_widget(self):
        self.rating_scale.configure(command=self.select, orient="horizontal",
                                    showvalue=False, tickinterval=1, to=5, length=250,
                                    bg="white", label="별점")
        self.close_button.configure(text="닫기", command=self.close)

        self.comment_edit_text.configure(font=self.TempFont, width=42, height=8, relief="solid")

        # Text 객체와 Scrollbar 객체의 연결
        self.comment_edit_text["yscrollcommand"] = self.comment_edit_scrollbar.set
        self.comment_edit_scrollbar["command"] = self.comment_edit_text.yview

    def place_widget(self):
        self.rating_scale.place(x=125, y=75)
        self.image_label.place(x=25, y=10)
        self.close_button.place(x=350, y=10)

        self.comment_edit_text.pack(side="left")
        self.comment_edit_scrollbar.pack(side="right", fill="y")
        self.comment_edit_frame.place(x=25, y=150)

    def open(self, book, image):
        self.book = book
        self.image_label["image"] = image
        self.frame.place(x=self.position[0], y=self.position[1], anchor="n")
        self.frame.tkraise()
        print("열려라")

    def close(self):
        self.frame.place_forget()

    def select(self, event):
        pass