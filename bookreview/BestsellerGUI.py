from tkinter import *
from tkinter import ttk
from tkinter import font
from Bestseller_Search_engine import  BestsellerSearchEngine
from urlImage import UrlImage
from datetime import date, datetime, timedelta
import Sounds

TEXT_START = 1.0
TEXT_END = END

class BestsellerGUI:
    root = None
    window = None

    title_font = None

    title_label = None
    close_button = None

    bsbooks=None

    def __init__(self, frame):
        self.root = frame
        self.frame = Frame(frame, width=1000, height=600)

        self.set_font()

        self.set_widget()
        self.place_widget()

    def set_widget(self):
        self.frame.configure(bg="beige", bd=3, relief="ridge")

        self.bsbooks = BSbooks(self.frame, x=500, y=100)
        self.title_label = Label(self.frame, font=self.title_font, text="★ "+str(date.today()) + " 오늘의 BEST SELLER ★", bg="beige")
        self.close_button = Button(self.frame, text="close", command=self.frame.place_forget)

    def place_widget(self):
        self.title_label.place(x=500, y=30, anchor="n")
        self.close_button.place(x=900, y=30)

    def set_font(self):
        self.title_font = font.Font(family="메이플스토리", weight="bold", size=25)

    def show_window(self):
        self.frame.place(x=0, y=0)
        self.frame.tkraise()
        Sounds.띠리리링()


class BSbooks:

    BS_engine=None

    # result frame
    result_listbox = None
    result_scrollbar = None

    category=100
    v=0


    def __init__(self, frame, x, y):
        self.TempFont = font.Font(size=14, weight='bold', family='메이플스토리')
        self.detail_font = font.Font(size=12, weight='bold', family='메이플스토리')
        self.big_font = font.Font(size=20, weight='bold', family='메이플스토리')

        self.create_widget(frame)
        self.place_widget()

        self.BS_engine=BestsellerSearchEngine()
        self.search_books()

    def create_widget(self, frame):
        self.setting_frame = Frame(frame, bg="white", width=200, height=50)
        self.detail_frame = Frame(frame, bg="white", width=420, height=335)
        self.result_frame = Frame(frame, bg="white", width=420, height=330)
        self.image_frame = Frame(frame, width=420, height=335, bg="beige")

        #setting
        self.v=IntVar()
        Radiobutton(self.setting_frame,text="국내",variable=self.v, value=1,
                    command=self.search_books,font=self.big_font,bg="beige").pack(side=LEFT)
        Radiobutton(self.setting_frame, text="국외", variable=self.v,value=2,
                    command=self.search_books,font=self.big_font,bg="beige").pack(side=LEFT)

        #image
        self.book_image = PhotoImage(file="Resource/Image/bear.png")
        self.image_label = Label(self.image_frame, image=self.book_image, bg="beige")
        self.image_label.grid(row=0, column=0)

        # result
        self.result_scrollbar = Scrollbar(self.result_frame)
        self.result_listbox = Listbox(self.result_frame, font=self.TempFont, width=30, height=15, activestyle="none",
                                      selectmode="single", yscrollcommand=self.result_scrollbar.set)

        self.result_listbox.bind("<Double-Button-1>", self.show_detail)

        # detail
        self.result_listbox["yscrollcommand"] = self.result_scrollbar.set
        self.result_scrollbar["command"] = self.result_listbox.yview

        self.image_label = Label(self.detail_frame, bg="white", bd=1, relief="solid")
        self.title_label = Label(self.detail_frame, font=self.detail_font, text="제목", bg='white')
        self.author_label = Label(self.detail_frame, font=self.detail_font, text="저자", bg='white')
        self.publisher_label = Label(self.detail_frame, font=self.detail_font, text="출판사", bg='white')
        self.pubdate_label = Label(self.detail_frame, font=self.detail_font, text="출판일", bg='white')
        self.price_label = Label(self.detail_frame, font=self.detail_font, text="가격", bg='white')
        self.description_text = Text(self.detail_frame, font=self.detail_font, bg='white', width=35, height=6,
                                     relief="solid")

        self.back_to_list_button = Button(self.detail_frame, font=self.TempFont, text="목록으로",
                                          command=self.detail_frame.place_forget)

    def place_widget(self):
        self.setting_frame.place(x=200, y=100, anchor="n")
        self.result_frame.place(x=300, y=150, anchor="n")
        self.image_frame.place(x=730, y=150, anchor="n")

        self.result_listbox.pack(side="left")
        self.result_scrollbar.pack(side="right", fill='y')

        self.image_label.place(x=10, y=10)
        self.title_label.place(x=120, y=10)
        self.author_label.place(x=120, y=35)
        self.publisher_label.place(x=120, y=60)
        self.pubdate_label.place(x=120, y=85)
        self.price_label.place(x=120, y=110)
        self.description_text.place(x=210, y=150, anchor="n")

        self.back_to_list_button.place(x=10, y=300, anchor="w")

    def search_books(self, event=None):
        self.result_listbox.delete(0, self.result_listbox.size())
        if self.v.get()==2: #해외 선택시
            self.BS_engine.category=200
            Sounds.뿅()
        elif self.v.get()==1:
            self.BS_engine.category=100
            Sounds.뽁()

        self.BS_engine.set_search()

        for i, book in enumerate(self.BS_engine.searched_books):
            self.result_listbox.insert(i, str(i+1)+"위: "+book["title"])

        self.detail_frame.place_forget()  # detail창이 띄워진 상태일 수도 있으니 닫는다.

    def show_detail(self,event):
        selected_index = self.result_listbox.curselection()
        if selected_index == ():
            return

        self.selected_book = self.BS_engine.searched_books[selected_index[0]]

        self.url_image = UrlImage(self.selected_book["image"])

        self.image_label.configure(image=self.url_image.get_image())
        self.title_label.configure(text=f"제목: {self.selected_book['title']}")
        self.author_label.configure(text=f"저자: {self.selected_book['author']}")
        self.publisher_label.configure(text=f"출판사: {self.selected_book['publisher']}")
        self.pubdate_label.configure(text=f"출판일: {self.selected_book['pubDate']}")
        self.price_label.configure(text=f"가격: {self.selected_book['price']}")

        self.description_text.configure(state="normal")
        self.description_text.delete(TEXT_START, TEXT_END)
        self.description_text.insert(TEXT_START, self.selected_book["description"])
        self.description_text.configure(state="disable")

        self.detail_frame.place(x=730, y=150, anchor="n")
        self.detail_frame.tkraise()
        Sounds.뽁()
