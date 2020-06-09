from tkinter import *
from tkinter import ttk
from tkinter import font
import tkinter.messagebox
from bookSearchGUI import BookSearchGUI
from LibrarySearchGUI import LibrarySearchGUI
from RecordBookGUI import RecordBookGUI
from editGUI import EditGUI

class MainGUI:
    window = None
    TempFont = None
    title_font = None

    # Main Frame
    hud_frame = None
    image_frame = None
    book_frame = None
    library_frame = None
    left_frame = None

    # HUD Frame Widget
    title_label = None
    search_book_button = None
    search_library_button = None

    # Image Frame Widget
    book_image = None
    image_label = None

    # Book Search Frame Widget
    book_search_gui = None
    library_search_gui=None
    record_book_gui=None

    # Library Search Frame Widget
    library_setting_frame = None
    library_result_frame = None

    # Left Frame Widget
    edit_gui = None

    def __init__(self):
        self.window = Tk()

        self.set_font()
        self.set_window()
        self.build_main_frame()

        self.build_hud()
        self.build_image()

        self.build_book_search()
        self.build_library_search()
        self.build_left()

        self.link_gui()

        change_frame(self.book_frame)

        self.window.mainloop()

    def set_window(self):
        self.window.title("♥ 나만의 독서기록장 ♥")
        self.window.geometry("1000x600+200+100")
        self.window.resizable(False, False) #확대창 없애기
        self.window.configure(bg="beige")
        # 아이콘 모양 변경할 수 있음
        # self.window.iconbitmap(default="파일이름")
        self.window.option_add("*TCombobox*Listbox.font", self.TempFont) #콤보박스에 폰트넣기

    def set_font(self):
        self.title_font = font.Font(size=24, weight="bold", family="Consolas")
        self.TempFont = font.Font(size=14, weight='bold', family='Consolas')

    def build_main_frame(self):
        # Create
        self.hud_frame = Frame(self.window, width=500, height=100, bg="beige")
        self.image_frame = Frame(self.window, width=500, height=200, bg="beige")
        self.book_frame = Frame(self.window, width=500, height=500, bg="beige")
        self.library_frame = Frame(self.window, width=500, height=500, bg="beige")
        self.left_frame = Frame(self.window, width=500, height=500, bg="beige")

        # Place
        self.hud_frame.grid(row=0, column=0)
        self.image_frame.grid(row=0, column=1)
        self.book_frame.grid(row=1, column=0)
        self.library_frame.grid(row=1, column=0)
        self.left_frame.grid(row=1, column=1)

        # debug 용
        # self.hud_frame["bd"] = 1  #테두리 두께
        # self.image_frame["bd"] = 1
        # self.book_frame["bd"] = 1
        # self.library_frame["bd"] = 1
        # self.left_frame["bd"] = 1
        # self.hud_frame["relief"] = "solid" #테두리모양
        # self.image_frame["relief"] = "solid"
        # self.book_frame["relief"] = "solid"
        # self.library_frame["relief"] = "solid"
        # self.left_frame["relief"] = "solid"

    def build_image(self):
        self.book_image = PhotoImage(file="Resource/Image/Book.png")
        self.image_label = Label(self.image_frame, image=self.book_image,bg="beige")
        self.image_label.grid(row=0,column=0)
        self.book2_image = PhotoImage(file="Resource/Image/Book2.png")
        self.image_label = Label(self.image_frame, image=self.book2_image, bg="beige")
        self.image_label.grid(row=0, column=1)
        self.book3_image = PhotoImage(file="Resource/Image/Book3.png")
        self.image_label = Label(self.image_frame, image=self.book3_image, bg="beige")
        self.image_label.grid(row=0, column=2)
        self.book4_image = PhotoImage(file="Resource/Image/Book4.png")
        self.image_label = Label(self.image_frame, image=self.book4_image, bg="beige")
        self.image_label.grid(row=0, column=3)
        self.book5_image = PhotoImage(file="Resource/Image/Book5.png")
        self.image_label = Label(self.image_frame, image=self.book5_image, bg="beige")
        self.image_label.grid(row=0, column=4)

    def build_hud(self):
        # Create
        self.title_label = Label(self.hud_frame, font=self.title_font, text="♥ 나만의 독서기록장 ♥", bg="beige")
        self.search_book_button = Button(self.hud_frame, text="책 검색", width=11, height=1, font=self.TempFont,
                                         command=lambda: change_frame(self.book_frame))
        self.search_library_button = Button(self.hud_frame, text="도서관 찾기", width=11, height=1, font=self.TempFont,
                                            command=lambda: change_frame(self.library_frame))

        # Place
        self.title_label.place(x=250, y=10, anchor="n")     # x 중앙, y 상단이 기준
        self.search_book_button.place(x=40, y=65)
        self.search_library_button.place(x=175, y=65)

    def build_book_search(self):
        self.book_search_gui = BookSearchGUI(self.book_frame)

    def build_library_search(self):
        self.library_search_gui = LibrarySearchGUI(self.library_frame)

    def build_left(self):
        self.edit_gui = EditGUI(self.left_frame, 250, 130)
        self.record_book_gui = RecordBookGUI(self.left_frame)

    def link_gui(self):
        self.book_search_gui.set_edit_gui(self.edit_gui)

def change_frame(frame):
    frame.tkraise()


MainGUI()

