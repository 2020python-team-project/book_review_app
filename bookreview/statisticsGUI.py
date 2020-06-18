from tkinter import *
from tkinter import font


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
        self.close_button = Button(self.frame, font=self.button_font, text="닫기", command=self.frame.place_forget)

    def place_widget(self):
        self.title_label.place(x=500, y=30, anchor="n")
        self.close_button.place(x=900, y=30)

    def set_font(self):
        self.title_font = font.Font(family="메이플스토리", weight="bold", size=25)
        self.button_font = font.Font(family="메이플스토리", weight="bold", size=14)

    def show_window(self):
        self.graph.build_graph()

        self.frame.place(x=0, y=0)
        self.frame.tkraise()


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
    book_manager = None

    period = None

    total_date = dict()     # [ str(년월) : int(키에 해당하는 책 개수) ], 저장되어 있는 모든 책을 기간별로 분류한다.
    graph_data = dict()     # [ str(현재 보여지는 월) : int(키에 해당하는 책 개수) ], 현재 보여지는 월별로 책을 분류한다.

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

    def __init__(self, frame, x, y, book_manager):
        self.canvas = Canvas(frame, width=900, height=450, bg="white")
        self.default_font = font.Font(family="메이플스토리", weight="bold", size=14)
        self.image = PhotoImage(file="Resource/Image/book_stock.PNG")

        self.book_manager = book_manager

        self.debug()

        self.canvas.place(x=x, y=y, anchor="n")

    def build_graph(self):
        self.period = Period("2020", "상반기")
        self.set_widget_period(self.period)

        self.set_total_date()
        self.set_graph_data()

        self.draw_graph()

    def set_widget_period(self, period):
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
        for month, count in self.graph_data.items():
            for i in range(count):
                self.canvas.create_image(self.graph_xpos[month], 340-i*70, image=self.image)


    def debug(self):
        for i in range(9):
            self.canvas.create_line(i*100, 0, i*100, 450)


# test
if __name__ == "__main__":
    # window = Tk()
    #
    # window.geometry("1000x600")
    # statistics_window = StatisticsGUI(window)
    #
    # button = Button(window, text="click me", command=statistics_window.show_window)
    # button.pack()
    #
    # window.mainloop()
    pass
