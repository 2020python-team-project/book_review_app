from tkinter import *
from tkinter import ttk
from tkinter import font
import tkinter.messagebox
from bookSearchGUI import BookSearchGUI


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

    # Library Search Frame Widget
    library_setting_frame = None
    library_result_frame = None

    # Left Frame Widget

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

        change_frame(self.book_frame)

        self.window.mainloop()

    def set_window(self):
        self.window.title("♥ 나만의 독서기록장 ♥")
        self.window.geometry("1000x600+200+100")
        self.window.resizable(False, False)
        self.window.configure(bg="beige")
        self.window.option_add("*TCombobox*Listbox.font", self.TempFont)

    def set_font(self):
        self.title_font = font.Font(size=24, weight="bold", family="Consolas")
        self.TempFont = font.Font(size=14, weight='bold', family='Consolas')

    def build_main_frame(self):
        # Create
        self.hud_frame = Frame(self.window, width=500, height=100, bg="beige")
        self.image_frame = Frame(self.window, width=500, height=100, bg="beige")
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
        # self.hud_frame["bd"] = 1
        # self.image_frame["bd"] = 1
        # self.book_frame["bd"] = 1
        # self.library_frame["bd"] = 1
        # self.left_frame["bd"] = 1
        # self.hud_frame["relief"] = "solid"
        # self.image_frame["relief"] = "solid"
        # self.book_frame["relief"] = "solid"
        # self.library_frame["relief"] = "solid"
        # self.left_frame["relief"] = "solid"

    def build_image(self):
        # 이미지 왜 안 불림ㅠ
        # self.book_image = PhotoImage(file="Resource/Image/Book.png")
        self.image_label = Label(self.image_frame, image=self.book_image)

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
        # Create
        self.library_setting_frame = Frame(self.library_frame, bg="white", width=420, height=100)
        self.library_result_frame = Frame(self.library_frame, bg="white", width=420, height=330)

        # Place
        self.library_setting_frame.place(x=250, y=10, anchor="n")
        self.library_result_frame.place(x=250, y=130, anchor="n")

    def build_left(self):
        self.canvas = Canvas(self.left_frame, bg="white", width=420, height=330)
        self.canvas.place(x=30, y=130)
        self.Font = font.Font(size=15, weight='bold', family='Consolas')

        self.B3 = Button(self.left_frame, text="+", width=2, height=1, font=self.TempFont)
        self.B3.place(x=380, y=80)
        self.B4 = Button(self.left_frame, text="-", width=2, height=1, font=self.TempFont)
        self.B4.place(x=420, y=80)

        self.B5 = Button(self.left_frame, text="주간 통계보기", width=10, height=1, font=self.TempFont)
        self.B5.place(x=30, y=80)




def change_frame(frame):
    frame.tkraise()

MainGUI()

