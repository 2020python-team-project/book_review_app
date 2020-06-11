# -*- coding: cp949 -*-
from tkinter import *
from tkinter import font
from Record_search_engine import RecordSearchEngine
from statisticsGUI import StatisticsGUI


class RecordBookGUI:
    record_frame = None
    detail_frame = None

    plus_button=None
    minus_button=None
    statistic_button=None

    record_listbox = None
    record_scrollbar = None

    #detail
    back_to_list_button = None

    title_label = None
    author_label = None
    publisher_label = None

    # 통계 GUI
    statistic_gui = None

    RB_engine=None


    def __init__(self,frame):
        self.TempFont = font.Font(size=14, weight='bold', family='Consolas')
        self.small_font = font.Font(size=11, family='Consolas')

        self.RB_engine=RecordSearchEngine()
        self.statistic_gui = StatisticsGUI(frame)

        self.create_widget(frame)
        self.place_widget()
        self.record_list()

    def create_widget(self, frame):
        self.detail_frame = Frame(frame, bg="white", width=420, height=330)
        self.record_frame = Frame(frame, bg="white", width=420, height=330)

        self.plus_button = Button(frame, text="+", width=2, height=1, font=self.TempFont,
                                  command=self.plusBook)
        self.minus_button = Button(frame, text="-", width=2, height=1, font=self.TempFont,
                                   command=self.minusBook
                                   )
        self.statistic_button = Button(frame, text="주간 통계보기", width=14, height=1, font=self.TempFont,bg='plum3',
                                       command=self.statistic_gui.show_window)

        self.record_scrollbar = Scrollbar(self.record_frame)
        self.record_listbox = Listbox(self.record_frame, font=self.TempFont, width=40, height=14, activestyle="none",
                                      selectmode="single", yscrollcommand=self.record_scrollbar.set)

        self.record_listbox.bind("<Double-Button-1>", self.show_detail)

        self.back_to_list_button = Button(self.detail_frame, font=self.TempFont, text="목록으로",
                                          command=self.record_frame.tkraise)

        self.title_label = Label(self.detail_frame, font=self.small_font, text="제목", bg='white')
        self.author_label = Label(self.detail_frame, font=self.small_font, text="저자", bg='white')
        self.publisher_label = Label(self.detail_frame, font=self.small_font, text="출판사",bg='white')

    def place_widget(self):
        self.detail_frame.place(x=250, y=130, anchor="n")
        self.record_frame.place(x=250, y=130, anchor="n")

        self.plus_button.place(x=380, y=80)
        self.minus_button.place(x=420, y=80)
        self.statistic_button.place(x=40, y=80)

        self.record_listbox.pack(side="left")
        self.record_scrollbar.pack(side="right", fill='y')

        self.back_to_list_button.place(x=10, y=300, anchor="w")

        self.title_label.place(x=50, y=10)
        self.author_label.place(x=50, y=40)
        self.publisher_label.place(x=50, y=70)

    def record_list(self):
        if not self.checkDocument():  # DOM이 None인지 검사합니다.
            return None
        #self.books.clear()
        self.booklist = self.RB_engine.BooksDoc.childNodes
        self.book = self.booklist[0].childNodes
        i=0
        for item in self.book:
            if item.nodeName == "book":
                subitems = item.childNodes  # item 들어 있는 노드들을 가져옵니다.
                for atom in subitems:
                    if atom.nodeName in ["title",]:
                        self.record_listbox.insert(i,atom.firstChild.nodeValue)  # 책 목록을 출력 합니다.
                        i+=1

    def show_detail(self,event):
        selected_index = self.record_listbox.curselection()
        if selected_index == ():
            return
        selected_book = self.RB_engine.books[selected_index[0]]

        self.title_label["text"] = "제목: "+ selected_book.title
        self.author_label["text"] = "저자: "+ selected_book.author
        self.publisher_label["text"] = "출판사: "+ selected_book.publisher
        self.detail_frame.tkraise()

    def plusBook(self):
        print("plus!")

    def minusBook(self):
        pass

    def checkDocument(self):
        if self.RB_engine.BooksDoc == None:
            print("Error : Document is empty")
            return False
        return True

