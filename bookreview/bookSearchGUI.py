from tkinter import *
from tkinter import ttk
from tkinter import font
from urlImage import UrlImage
from book_search_engine import BookSearchEngine
from bookManager import BookManager


class BookSearchGUI:
    setting_frame = None
    result_frame = None
    detail_frame = None

    # setting frame
    book_search_button = None
    keyword_entry = None
    head_combobox = None
    book_catg_combobox = None
    rst_num_label = None

    # result frame
    result_listbox = None
    result_scrollbar = None

    # detail frame
    image_label = None
    url_image = None
    title_label = None
    author_label = None
    publisher_label = None
    pubdate_label = None
    price_label = None
    description_text = None
    link_label = None
    back_to_list_button = None
    save_button = None

    heads = ["제목", "저자", "출판사"]
    categories = ["전체", "소설", "시/에세이", "인문", "자기계발", "역사/문화", "해외도서"]
    head = str()
    category = str()
    display_num = int()
    start_num = int()

    edit_gui = None

    # data
    bsch_engine = None
    RB_engine = None

    selected_book = None

    def __init__(self, frame):
        self.default_font = font.Font(size=14, weight='bold', family='메이플스토리')
        self.detail_font = font.Font(family='메이플스토리', weight="bold", size=11)

        self.create_widget(frame)
        self.place_widget()

        # data
        self.bsch_engine = BookSearchEngine()
        # self.RB_engine = BookManager()

    def create_widget(self, frame):
        self.setting_frame = Frame(frame, bg="white", width=420, height=100)
        self.detail_frame = Frame(frame, bg="white", width=420, height=335)
        self.result_frame = Frame(frame, bg="white")

        self.keyword_entry = Entry(self.setting_frame, relief="solid", font=self.default_font, width=17)
        self.book_search_button = Button(self.setting_frame, text="검색", font=self.default_font, bg='indian red',
                                         command=self.search_books)
        self.keyword_entry.bind("<Return>", self.search_books)

        self.rst_num_label = Label(self.setting_frame, font=self.default_font, bg="white", text="검색 결과: ")
        self.head_combobox = \
            ttk.Combobox(self.setting_frame, font=self.default_font, values=self.heads, width=4, height=3, state="readonly")
        self.book_catg_combobox = \
            ttk.Combobox(self.setting_frame, font=self.default_font, values=self.categories, width=6, height=7, state="readonly")

        self.head_combobox.set(self.heads[0])
        self.book_catg_combobox.set(self.categories[0])

        self.result_listbox = Listbox(self.result_frame, font=self.default_font, width=30, height=15, activestyle="none",
                                      selectmode="single")
        self.result_listbox.bind("<Double-Button-1>", self.show_detail)     # 더블클릭하면 변환
        self.result_scrollbar = Scrollbar(self.result_frame)

        self.result_listbox["yscrollcommand"] = self.result_scrollbar.set
        self.result_scrollbar["command"] = self.result_listbox.yview

        self.image_label = Label(self.detail_frame, bg="white", bd=1, relief="solid")
        self.title_label = Label(self.detail_frame, font=self.detail_font, text="제목", bg='white')
        self.author_label = Label(self.detail_frame, font=self.detail_font, text="저자", bg='white')
        self.publisher_label = Label(self.detail_frame, font=self.detail_font, text="출판사", bg='white')
        self.pubdate_label = Label(self.detail_frame, font=self.detail_font, text="출판일", bg='white')
        self.price_label = Label(self.detail_frame, font=self.detail_font, text="가격", bg='white')
        self.description_text = Text(self.detail_frame, font=self.detail_font, bg='white', width=40, height=6, relief="solid")
        self.link_label = Label(self.detail_frame, font=self.detail_font, text="링크", bg='white')

        self.back_to_list_button = Button(self.detail_frame, font=self.default_font, text="목록으로",
                                          command=self.detail_frame.place_forget)
        self.save_button = Button(self. detail_frame, font=self.default_font, text="저장하기",
                                  command=self.open_edit_frame)

    def place_widget(self):
        # Place Widget
        self.setting_frame.place(x=250, y=10, anchor="n")
        self.result_frame.place(x=250, y=130, anchor="n")

        self.keyword_entry.place(x=100, y=30, anchor="w")
        self.book_search_button.place(x=340, y=30, anchor="w")
        self.head_combobox.place(x=20, y=30, anchor="w")
        self.rst_num_label.place(x=20, y=75, anchor="w")
        self.book_catg_combobox.place(x=300, y=75, anchor="w")

        self.result_listbox.pack(side="left")
        self.result_scrollbar.pack(side="right", fill='y')

        self.image_label.place(x=10, y=10)
        self.title_label.place(x=120, y=10)
        self.author_label.place(x=120, y=35)
        self.publisher_label.place(x=120, y=60)
        self.pubdate_label.place(x=120, y=85)
        self.price_label.place(x=120, y=110)
        self.description_text.place(x=210, y=150, anchor="n")
        # self.link_label.place(x=10, y=250) 버튼을 만들어서 웹이랑 연결하자

        self.back_to_list_button.place(x=10, y=300, anchor="w")
        self.save_button.place(x=320, y=300, anchor="w")

    def search_books(self, event=None):
        # 스크롤을 아래로 계속 내리면 검색 결과를 더 불러오는 기능 구현해야 함..
        self.bsch_engine.set_search_word(self.keyword_entry.get())
        self.bsch_engine.set_display_num()
        self.bsch_engine.set_start_num()
        self.bsch_engine.set_category(self.book_catg_combobox.get())

        self.bsch_engine.request_search_result(self.head_combobox.get())

        self.rst_num_label["text"] = "검색 결과: " + str(self.bsch_engine.get_total()) + "건"
        self.add_book_in_list()

    def add_book_in_list(self):
        self.result_listbox.delete(0, self.result_listbox.size())
        for i, book in enumerate(self.bsch_engine.books):
            self.result_listbox.insert(i, book.title)

    def show_detail(self, event):
        selected_index = self.result_listbox.curselection()
        if selected_index == ():
            return
        self.selected_book = self.bsch_engine.books[selected_index[0]]

        self.selected_book.print_info()

        self.url_image = UrlImage(self.selected_book.image)

        self.image_label["image"] = self.url_image.get_image()
        self.title_label["text"] = "제목: " + self.selected_book.title
        self.author_label["text"] = "저자: " + self.selected_book.author
        self.publisher_label["text"] = "출판사: " + self.selected_book.publisher
        self.pubdate_label["text"] = "출판일: " + self.selected_book.pubdate
        self.price_label["text"] = "가격: " + self.selected_book.price

        self.description_text.delete(1.0, END)      # 처음부터 끝까지 텍스트 창에 있는 내용을 비운다
        self.description_text.insert(1.0, self.selected_book.description)
        # self.description_text["state"] = "disable"
        self.link_label["text"] = "링크: " + self.selected_book.link

        self.detail_frame.place(x=250, y=130, anchor="n")
        self.detail_frame.tkraise()

    def set_edit_gui(self, gui):
        self.edit_gui = gui

    def open_edit_frame(self):
        if self.edit_gui is not None:
            self.edit_gui.open(self.selected_book, self.url_image.get_image())
        self.detail_frame.place_forget()

    def save_book(self):
        # # 엘리먼트를 만듭니다.
        # newBook = self.RB_engine.BooksDoc.createElement('book')
        # titleEle = self.RB_engine.BooksDoc.createElement('title')
        # titleNode = self.RB_engine.BooksDoc.createTextNode(self.selected_book.title)
        #
        # # 텍스트 노드와 Title 엘리먼트를 연결 시킵니다.
        # try:
        #     titleEle.appendChild(titleNode)
        # except Exception:
        #     print("append child fail- please,check the parent element & node!!!")
        #     return None
        # else:
        #     titleEle.appendChild(titleNode)
        #
        # # Title을 book 엘리먼트와 연결 시킵니다.
        # try:
        #     newBook.appendChild(titleEle)
        #     booklist = self.RB_engine.BooksDoc.firstChild
        # except Exception:
        #     print("append child fail- please,check the parent element & node!!!")
        #     return None
        # else:
        #     if booklist != None:
        #         booklist.appendChild(newBook)
        #         print(booklist.toprettyxml())
        #         # 앨리먼트와 텍스트 추가는 했고.. record 창 갱신은 어떻게?
        pass
