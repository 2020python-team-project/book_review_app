from tkinter import *
from tkinter import font
from bookSearchGUI import BookSearchGUI
from LibrarySearchGUI import LibrarySearchGUI
from RecordBookGUI import RecordBookGUI
from editGUI import EditGUI
from statisticsGUI import StatisticsGUI
from BestsellerGUI import BestsellerGUI
import rating_image
from bookManager import BookManager

class MainGUI:
    window = None
    button_font = None
    title_font = None

    # Main Frame
    hud_frame = None
    image_frame = None
    book_frame = None
    library_frame = None
    bookcase_frame = None

    # HUD Frame Widget
    title_label = None
    search_book_button = None
    search_library_button = None

    # Image Frame Widget
    book_image = None
    image_label = None

    # Book Search Frame Widget
    book_search_gui = None
    library_search_gui = None
    record_book_gui = None

    # Library Search Frame Widget
    library_setting_frame = None
    library_result_frame = None

    # Left Frame Widget
    edit_gui = None

    # 통계 GUI
    statistic_gui = None

    book_manager = None

    def __init__(self):
        self.window = Tk()

        self.set_font()
        rating_image.load_image()

        self.book_manager = BookManager()

        self.set_window()
        self.build_main_frame()

        self.build_hud()
        self.build_image()

        self.build_book_search()
        self.build_library_search()
        self.build_bookcase()

        self.link_gui()



        change_frame(self.book_frame)

    def set_font(self):
        self.title_font = font.Font(size=24, weight="bold", family="메이플스토리")
        self.button_font = font.Font(size=15, weight='bold', family='메이플스토리')

    def set_window(self):
        self.window.title("♥ 나만의 독서기록장 ♥")
        self.window.geometry("1000x600+200+100")
        self.window.resizable(False, False)     # 확대창 없애기
        self.window.configure(bg="beige")
        # 아이콘 모양 변경할 수 있음
        # self.window.iconbitmap(default="파일이름")
        self.window.option_add("*TCombobox*Listbox.font", self.button_font)    # 콤보박스에 폰트넣기

    def build_main_frame(self):
        # Create
        self.hud_frame = Frame(self.window, width=500, height=100, bg="beige")
        self.image_frame = Frame(self.window, width=500, height=200, bg="beige")
        self.book_frame = Frame(self.window, width=500, height=500, bg="beige")
        self.library_frame = Frame(self.window, width=500, height=500, bg="beige")
        self.bookcase_frame = Frame(self.window, width=500, height=500, bg="beige")

        # Place
        self.hud_frame.grid(row=0, column=0)
        self.image_frame.grid(row=0, column=1)
        self.book_frame.grid(row=1, column=0)
        self.library_frame.grid(row=1, column=0)
        self.bookcase_frame.grid(row=1, column=1)

        # debug 용
        # self.hud_frame.configure(bd=1, relief="solid")
        # self.image_frame.configure(bd=1, relief="solid")
        # self.book_frame.configure(bd=1, relief="solid")
        # self.library_frame.configure(bd=1, relief="solid")
        # self.bookcase_frame.configure(bd=1, relief="solid")

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
        self.search_book_button = Button(self.hud_frame, text="책 검색", width=8, height=1, font=self.button_font, bg='DarkOliveGreen3',
                                         command=lambda: change_frame(self.book_frame))
        self.search_library_button = Button(self.hud_frame, text="도서관 찾기", width=8, height=1, font=self.button_font, bg='DarkOliveGreen3',
                                            command=lambda: change_frame(self.library_frame))

        # Place
        self.title_label.place(x=250, y=10, anchor="n")     # x 중앙, y 상단이 기준
        self.search_book_button.place(x=40, y=65)
        self.search_library_button.place(x=175, y=65)

    def build_book_search(self):
        self.book_search_gui = BookSearchGUI(self.book_frame)
        self.edit_gui = EditGUI(self.book_frame, 250, 10)

    def build_library_search(self):
        self.library_search_gui = LibrarySearchGUI(self.library_frame)

    def build_bookcase(self):
        self.record_book_gui = RecordBookGUI(self.bookcase_frame, self.book_manager)
        self.statistic_gui = StatisticsGUI(self.window, self.book_manager)
        self.Bestseller_gui = BestsellerGUI(self.window)
        self.edit_gui.debug()

    def link_gui(self):
        self.book_search_gui.set_edit_gui(self.edit_gui)
        self.edit_gui.link(book_manager=self.record_book_gui.book_manager)
        self.record_book_gui.set_statistics_gui(self.statistic_gui)
        self.record_book_gui.set_bestseller_gui(self.Bestseller_gui)
        self.book_manager.set_record_ui(self.record_book_gui)

    def run(self):
        self.window.mainloop()


def change_frame(frame):
    frame.tkraise()


main = MainGUI()
main.run()