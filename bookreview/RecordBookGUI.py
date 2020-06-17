# -*- coding: cp949 -*-
from tkinter import *
from tkinter import font
from bookManager import BookManager
from recordDetailGUI import RecordDetailGUI
from BestsellerGUI import BestsellerGUI


class RecordBookGUI:
    record_frame = None
    detail_frame = None

    plus_button = None
    minus_button = None
    statistic_button = None
    bestseller_button=None

    record_listbox = None
    record_scrollbar = None

    # detail
    detail_gui = None

    statistic_gui = None
    bestseller_gui = None

    book_manager = None

    def __init__(self, frame):
        self.TempFont = font.Font(size=14, weight='bold', family='메이플스토리')
        self.small_font = font.Font(size=11, family='메이플스토리')

        self.book_manager = BookManager(self)

        self.create_widget(frame)
        self.place_widget()
        self.update_record_list()

    def create_widget(self, frame):
        self.record_frame = Frame(frame, bg="white", width=420, height=330)

        self.plus_button = Button(frame, text="+", width=2, height=1, font=self.TempFont,
                                  command=self.plusBook)
        self.minus_button = Button(frame, text="-", width=2, height=1, font=self.TempFont,
                                   command=self.minusBook)
        self.statistic_button = Button(frame, text="주간 통계보기", width=14, height=1, font=self.TempFont, bg='plum3')
        self.bestseller_button = Button(frame, text="오늘의 베스트셀러", width=14, height=1, font=self.TempFont, bg='pink')

        self.record_scrollbar = Scrollbar(self.record_frame)
        self.record_listbox = Listbox(self.record_frame, font=self.TempFont, width=30, height=15, activestyle="none",
                                      selectmode="single", yscrollcommand=self.record_scrollbar.set)

        self.record_listbox.bind("<Double-Button-1>", self.show_detail)

        self.detail_gui = RecordDetailGUI(frame, 250, 10)

    def place_widget(self):
        self.record_frame.place(x=250, y=130, anchor="n")

        self.plus_button.place(x=380, y=20)
        self.minus_button.place(x=420, y=20)
        self.statistic_button.place(x=40, y=20)
        self.bestseller_button.place(x=40,y=70)

        self.record_listbox.pack(side="left")
        self.record_scrollbar.pack(side="right", fill='y')

    def update_record_list(self):
        self.record_listbox.delete(0, self.record_listbox.size())       # 원래 리스트 박스에 있던거 모두 삭제
        for i, book in enumerate(self.book_manager.books):
            self.record_listbox.insert(i, book.title)

    def show_detail(self, event):
        selected_index = self.record_listbox.curselection()
        if selected_index == ():
            return
        selected_book = self.book_manager.books[selected_index[0]]

        self.detail_gui.open(selected_book)

    def set_statistics_gui(self, gui):
        self.statistic_gui = gui
        self.statistic_button.configure(command=self.statistic_gui.show_window)

    def set_bestseller_gui(self, gui):
        self.Bestseller_gui = gui
        self.bestseller_button.configure(command=self.Bestseller_gui.show_window)

    def plusBook(self):
        print("plus!")

    def minusBook(self):
        pass

    def checkDocument(self):
        if self.book_manager.BooksDoc == None:
            print("Error : Document is empty")
            return False
        return True

