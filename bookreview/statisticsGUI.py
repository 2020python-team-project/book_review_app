from tkinter import *
from tkinter import ttk
from tkinter import font


class StatisticsGUI:
    root = None
    window = None

    title_font = None

    title_label = None
    close_button = None

    graph = None

    def __init__(self, frame):
        self.root = frame
        self.frame = Frame(frame, width=1000, height=600)

        self.set_font()

        self.set_widget()
        self.place_widget()

    def set_widget(self):
        self.frame.configure(bg="beige", bd=3, relief="ridge")

        self.graph = Graph(self.frame, x=500, y=100)
        self.title_label = Label(self.frame, font=self.title_font, text="통계", bg="beige")
        self.close_button = Button(self.frame, text="close", command=self.frame.place_forget)

    def place_widget(self):
        self.title_label.place(x=500, y=30, anchor="n")
        self.close_button.place(x=900, y=30)

    def set_font(self):
        self.title_font = font.Font(family="메이플스토리", weight="bold", size=25)

    def show_window(self):
        self.frame.place(x=0, y=0)
        self.frame.tkraise()


class Graph:
    canvas = None

    def __init__(self, frame, x, y):
        self.canvas = Canvas(frame, width=900, height=450, bg="white")
        self.canvas.place(x=x, y=y, anchor="n")


# test
if __name__ == "__main__":
    window = Tk()

    window.geometry("1000x600")
    statistics_window = StatisticsGUI(window)

    button = Button(window, text="click me", command=statistics_window.show_window)
    button.pack()

    window.mainloop()
