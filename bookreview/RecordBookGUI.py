# -*- coding: cp949 -*-
from tkinter import *
from tkinter import font
from tkinter import ttk
from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree

class RecordBookGUI:
    record_frame = None
    detail_frame = None

    plus_button=None
    minus_button=None
    statis_button=None

    record_listbox = None
    record_scrollbar = None

    back_to_list_button = None
    BooksDoc = None

    xmlFD = -1

    def __init__(self,frame):
        self.TempFont = font.Font(size=14, weight='bold', family='Consolas')
        self.small_font = font.Font(size=11, family='Consolas')

        self.BooksDoc=self.LoadXMLFromFile()
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
        self.statis_button = Button(frame, text="주간 통계보기", width=10, height=1, font=self.TempFont)

        self.record_scrollbar = Scrollbar(self.record_frame)
        self.record_listbox = Listbox(self.record_frame, font=self.TempFont, width=40, height=14, activestyle="none",
                                      selectmode="single", yscrollcommand=self.record_scrollbar.set)

        self.record_listbox.bind("<Double-Button-1>", self.show_detail)

        self.back_to_list_button = Button(self.detail_frame, font=self.TempFont, text="목록으로",
                                          command=self.record_frame.tkraise)

    def place_widget(self):
        self.detail_frame.place(x=250, y=130, anchor="n")
        self.record_frame.place(x=250, y=130, anchor="n")

        self.plus_button.place(x=380, y=80)
        self.minus_button.place(x=420, y=80)
        self.statis_button.place(x=40, y=80)

        self.record_listbox.pack(side="left")
        self.record_scrollbar.pack(side="right", fill='y')

        self.back_to_list_button.place(x=10, y=300, anchor="w")

    def record_list(self):
        if not self.checkDocument():  # DOM이 None인지 검사합니다.
            return None

        booklist = self.BooksDoc.childNodes
        book = booklist[0].childNodes
        i=0
        for item in book:
            if item.nodeName == "book":
                subitems = item.childNodes  # item 들어 있는 노드들을 가져옵니다.
                for atom in subitems:
                    if atom.nodeName in ["title",]:
                        self.record_listbox.insert(i,atom.firstChild.nodeValue)  # 책 목록을 출력 합니다.
                        i+=1
    def LoadXMLFromFile(self):
        global xmlFD

        try:
            xmlFD = open("book.xml")  # xml 문서를 open합니다.
        except IOError:
            print("invalid file name or path")
            return None
        else:
            try:
                dom = parse(xmlFD)  # XML 문서를 파싱합니다.
            except Exception:
                print("loading fail!!!")
            else:
                print("XML Document loading complete")
                print(dom.toprettyxml())
                return dom
        return None

    def show_detail(self,event):
        selected_index = self.record_listbox.curselection()
        if selected_index == ():
            return
        self.detail_frame.tkraise()

    def plusBook(self):
        pass

    def minusBook(self):
        pass

    def checkDocument(self):
        if self.BooksDoc == None:
            print("Error : Document is empty")
            return False
        return True

