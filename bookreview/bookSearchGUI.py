from tkinter import *
from tkinter import ttk
from tkinter import font
from book_search_engine import BookSearchEngine

class BookSearchGUI:
    book_setting_frame = None
    book_result_frame = None

    book_search_button = None
    keyword_entry = None
    book_head_combobox = None
    book_catg_combobox = None

    book_listbox = None
    book_scrollbar = None

    heads = ["제목", "저자", "출판사"]
    categories = ["전체", "소설", "시/에세이", "인문", "자기계발", "역사/문화", "해외도서"]
    head = str()
    category = str()
    display_num = int()
    start_num = int()

    # data
    bsch_engine = None

    def __init__(self, frame):
        self.TempFont = font.Font(size=14, weight='bold', family='Consolas')
        self.create_widget(frame)
        self.place_widget()

        # data
        self.bsch_engine = BookSearchEngine()
        self.head = "title"
        self.category = ""
        self.display_num = 15
        self.start_num = 1

    def create_widget(self, frame):
        self.book_setting_frame = Frame(frame, bg="white", width=420, height=100)
        self.book_result_frame = Frame(frame, bg="white", width=420, height=330)

        self.keyword_entry = Entry(self.book_setting_frame, relief="solid", font=self.TempFont)
        self.book_search_button = Button(self.book_setting_frame, text="검색", font=self.TempFont,
                                         command=self.search_books)
        self.book_head_combobox = \
            ttk.Combobox(self.book_setting_frame, font=self.TempFont, values=self.heads, width=6, height=3, state="readonly")
        self.book_catg_combobox = \
            ttk.Combobox(self.book_setting_frame, font=self.TempFont, values=self.categories, width=10, height=7, state="readonly")

        self.book_head_combobox.set(self.heads[0])
        self.book_catg_combobox.set(self.categories[0])

        self.book_scrollbar = Scrollbar(self.book_result_frame)
        self.book_listbox = Listbox(self.book_result_frame, font=self.TempFont,
                                    yscrollcommand=self.book_scrollbar.set)

    def place_widget(self):
        # Place Widget
        self.book_setting_frame.place(x=250, y=10, anchor="n")
        self.book_result_frame.place(x=250, y=130, anchor="n")
        self.keyword_entry.place(x=120, y=30, anchor="w")
        self.book_search_button.place(x=340, y=30, anchor="w")
        self.book_head_combobox.place(x=20, y=30, anchor="w")
        self.book_catg_combobox.place(x=270, y=70, anchor="w")
        self.book_listbox.pack(side="left")
        self.book_scrollbar.pack(side="right", fill='y')

    def search_books(self):
        self.bsch_engine.set_search_word(self.keyword_entry.get())
        self.bsch_engine.set_display_num(self.display_num)
        self.bsch_engine.set_start_num(self.start_num)
        self.bsch_engine.set_category(self.category)

        self.bsch_engine.request_search_result(self.head)
        self.add_book_in_list()

    def add_book_in_list(self):
        self.book_listbox.delete(0, len(self.bsch_engine.books))
        for i, book in enumerate(self.bsch_engine.books):
            self.book_listbox.insert(i, book.title)
