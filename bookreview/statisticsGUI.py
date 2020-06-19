from tkinter import *
from tkinter import font
from urlImage import UrlImage

class StatisticsGUI:
    root = None
    window = None

    title_font = None
    button_font = None

    title_label = None
    close_button = None

    graph = None

    book_manager = None

    def __init__(self, frame, book_manager):
        self.root = frame
        self.frame = Frame(frame, width=1000, height=600)

        self.set_font()
        self.book_manager = book_manager

        self.set_widget()
        self.place_widget()

    def set_widget(self):
        self.frame.configure(bg="beige", bd=3, relief="ridge")

        self.graph = Graph(self.frame, x=500, y=100, book_manager=self.book_manager)
        self.title_label = Label(self.frame, font=self.title_font, text="통계", bg="beige")
        self.close_button = Button(self.frame, font=self.button_font, text="닫기", command=self.close)

    def place_widget(self):
        self.title_label.place(x=500, y=30, anchor="n")
        self.close_button.place(x=900, y=30)

    def set_font(self):
        self.title_font = font.Font(family="메이플스토리", weight="bold", size=25)
        self.button_font = font.Font(family="메이플스토리", weight="bold", size=14)

    def show_window(self):
        self.frame.place(x=0, y=0)
        self.frame.tkraise()

        self.graph.build_graph()

    def close(self):
        self.graph.clear()
        self.frame.place_forget()


class Period:
    month_range = {
        "상반기": range(1, 7),
        "하반기": range(7, 13)
    }

    def __init__(self, year, half):
        self.year = year
        self.half = half

    def get_month_range(self):
        return self.month_range[self.half]


class Graph:
    canvas = None
    image = None
    default_font = None
    info_font = None
    book_manager = None

    period = None

    total_date = dict()     # [ str(YYYYMM) : int(키에 해당하는 책 개수) ], 저장되어 있는 모든 책을 기간별로 분류한다.
    graph_data = dict()     # [ str(MM) : int(키에 해당하는 책 개수) ], 현재 보여지는 월별로 책을 분류한다.

    graph_xpos = {
        "01": 100,
        "07": 100,
        "02": 200,
        "08": 200,
        "03": 300,
        "09": 300,
        "04": 400,
        "10": 400,
        "05": 500,
        "11": 500,
        "06": 600,
        "12": 600,
    }

    id_to_book = dict()

    cover_image = None
    info_rect_id = None
    cover_image_id = None
    title_text_id = None
    date_text_id = None

    def __init__(self, frame, x, y, book_manager):
        self.canvas = Canvas(frame, width=900, height=450, bg="white")
        self.default_font = font.Font(family="메이플스토리", weight="bold", size=14)
        self.info_font = font.Font(family="메이플스토리", weight="bold", size=12)
        self.image = PhotoImage(file="Resource/Image/book_stock.PNG")

        self.book_manager = book_manager

        self.period = Period("2020", "상반기")
        self.create_period_object(self.period)
        self.create_info_object()
        # self.debug()

        self.canvas.place(x=x, y=y, anchor="n")

    def build_graph(self):
        self.set_total_date()
        self.set_graph_data()

        self.draw_graph()

    def create_period_object(self, period):
        self.canvas.create_text(350, 30, font=self.default_font, text=f"{period.year}년 {period.half}")

        for i, month in enumerate(period.get_month_range()):
            self.canvas.create_text(i*100 + 100, 400, text=f"{month}월", font=self.default_font)

    def set_total_date(self):
        # 저장된 책의 편집 기간을 분류한다.
        self.total_date = dict()

        date_list = []

        for book in self.book_manager.books:
            date_list.append(book.edit_date[:6])

        for date in date_list:
            if date in self.total_date:
                self.total_date[date] += 1
            else:
                self.total_date[date] = 1

    def set_graph_data(self):
        for month in self.period.get_month_range():
            self.graph_data[str(month).zfill(2)] = 0

        for date in self.total_date.keys():
            year = date[:4]
            month = date[4:7]

            if year == self.period.year:        # 현재 보여지는 기간과 같은 해
                if month in self.graph_data:    # 같은 월이 그래프 데이터에 있으면
                    self.graph_data[month] = self.total_date[date]

        print(self.graph_data)

    def draw_graph(self):
        self.id_to_book.clear()
        for month, count in self.graph_data.items():
            books = self.get_book_list(month)

            for i in range(count):
                item = self.canvas.create_image(self.graph_xpos[month], 340 - i * 70, image=self.image)
                self.id_to_book[item] = books[i]
                self.canvas.after(300)
                self.canvas.update()

        for book_id in self.id_to_book.keys():
            self.canvas.tag_bind(book_id, "<Enter>", lambda event, b_id=book_id: self.show_info(b_id))
            self.canvas.tag_bind(book_id, "<Leave>", lambda event, b_id=book_id: self.close_info(b_id))

    def show_info(self, obj_id):
        self.cover_image = UrlImage(self.id_to_book[obj_id].image).get_image()

        self.canvas.itemconfigure(self.info_rect_id, state="normal")
        self.canvas.itemconfigure(self.cover_image_id, state="normal", image=self.cover_image)
        self.canvas.itemconfigure(self.title_text_id, state="normal", text=self.id_to_book[obj_id].title)
        self.canvas.itemconfigure(self.date_text_id, state="normal", text=self.id_to_book[obj_id].edit_date)

    def close_info(self, obj_id):
        self.canvas.itemconfigure(self.info_rect_id, state="hidden")
        self.canvas.itemconfigure(self.cover_image_id, state="hidden")
        self.canvas.itemconfigure(self.title_text_id, state="hidden")
        self.canvas.itemconfigure(self.date_text_id, state="hidden")

    def create_info_object(self):
        self.info_rect_id = self.canvas.create_rectangle(700, 50, 850, 400, state="hidden")
        self.cover_image_id = self.canvas.create_image(775, 130, state="hidden")
        self.title_text_id = self.canvas.create_text(775, 250, font=self.info_font, state="hidden", width=150)
        self.date_text_id = self.canvas.create_text(775, 350, font=self.info_font, state="hidden")

    def get_book_list(self, month):
        cur_date = self.period.year + month
        book_list = []
        for book in self.book_manager.books:
            if book.edit_date[:6] == cur_date:
                book_list.append(book)

        return book_list

    def clear(self):
        self.canvas.delete(ALL)

    def debug(self):
        for i in range(9):
            self.canvas.create_line(i*100, 0, i*100, 450)


if __name__ == "__main__":
    pass
