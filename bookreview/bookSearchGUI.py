from tkinter import *
from tkinter import ttk
from tkinter import font
from urlImage import UrlImage
from book_search_engine import BookSearchEngine


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
    description_label = None
    link_label = None
    back_to_list_button = None
    save_button = None

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
        self.detail_font = font.Font(size=10, family='Consolas')

        self.create_widget(frame)
        self.place_widget()

        # data
        self.bsch_engine = BookSearchEngine()

    def create_widget(self, frame):
        self.setting_frame = Frame(frame, bg="white", width=420, height=100)
        self.detail_frame = Frame(frame, bg="white", width=420, height=330)
        self.result_frame = Frame(frame, bg="white", width=420, height=330)

        self.keyword_entry = Entry(self.setting_frame, relief="solid", font=self.TempFont)
        self.book_search_button = Button(self.setting_frame, text="검색", font=self.TempFont,
                                         command=self.search_books)
        self.keyword_entry.bind("<Return>", self.search_books)

        self.rst_num_label = Label(self.setting_frame, font=self.TempFont, bg="white", text="검색 결과: ")
        self.head_combobox = \
            ttk.Combobox(self.setting_frame, font=self.TempFont, values=self.heads, width=6, height=3, state="readonly")
        self.book_catg_combobox = \
            ttk.Combobox(self.setting_frame, font=self.TempFont, values=self.categories, width=10, height=7, state="readonly")

        self.head_combobox.set(self.heads[0])
        self.book_catg_combobox.set(self.categories[0])

        self.result_scrollbar = Scrollbar(self.result_frame)
        self.result_listbox = Listbox(self.result_frame, font=self.TempFont, width=40, height=14, activestyle="none",
                                      selectmode="single", yscrollcommand=self.result_scrollbar.set)
        self.result_listbox.bind("<Double-Button-1>", self.show_detail) #더블클릭하면 변환

        self.image_label = Label(self.detail_frame)
        self.title_label = Label(self.detail_frame, font=self.detail_font, text="제목")
        self.author_label = Label(self.detail_frame, font=self.detail_font, text="저자")
        self.publisher_label = Label(self.detail_frame, font=self.detail_font, text="출판사")
        self.pubdate_label = Label(self.detail_frame, font=self.detail_font, text="출판일")
        self.price_label = Label(self.detail_frame, font=self.detail_font, text="가격")
        self.description_label = Label(self.detail_frame, font=self.detail_font, text="설명")
        self.link_label = Label(self.detail_frame, font=self.detail_font, text="링크")
        self.back_to_list_button = Button(self.detail_frame, font=self.detail_font, text="목록으로",
                                          command=self.result_frame.tkraise)
        self.save_button = Button(self. detail_frame, font=self.detail_font, text="저장하기",
                                  command=self.open_save_frame)

    def place_widget(self):
        # Place Widget
        self.setting_frame.place(x=250, y=10, anchor="n")
        self.detail_frame.place(x=250, y=130, anchor="n")
        self.result_frame.place(x=250, y=130, anchor="n")

        self.keyword_entry.place(x=120, y=30, anchor="w")
        self.book_search_button.place(x=340, y=30, anchor="w")
        self.head_combobox.place(x=20, y=30, anchor="w")
        self.rst_num_label.place(x=20, y=75, anchor="w")
        self.book_catg_combobox.place(x=270, y=75, anchor="w")

        self.result_listbox.pack(side="left")
        self.result_scrollbar.pack(side="right", fill='y')

        self.image_label.pack()
        self.image_label.place(x=10, y=10)
        self.title_label.place(x=150, y=10)
        self.author_label.place(x=150, y=40)
        self.publisher_label.place(x=150, y=70)
        self.pubdate_label.place(x=150, y=100)
        self.price_label.place(x=150, y=130)
        self.description_label.place(x=10, y=160)
        self.link_label.place(x=10, y=240)
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
        selected_book = self.bsch_engine.books[selected_index[0]]

        self.url_image = UrlImage(selected_book.image)

        self.image_label["image"] = self.url_image.get_image()
        self.title_label["text"] = "제목: " + selected_book.title
        self.author_label["text"] = "저자: " + selected_book.author
        self.publisher_label["text"] = "출판사: " + selected_book.publisher
        self.pubdate_label["text"] = "출판일: " + selected_book.pubdate
        self.price_label["text"] = "가격: " + selected_book.price
        self.description_label["text"] = "설명: " + selected_book.description
        self.link_label["text"] = "링크: " + selected_book.link

        self.detail_frame.tkraise()

    def open_save_frame(self):
        pass
