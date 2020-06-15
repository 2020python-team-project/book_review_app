from tkinter import *
from tkinter import ttk
from tkinter import font


# 새로운 윈도우 창보단 화면 가득 덮는 새 프래임이 나을 듯
class StatisticsGUI:
    root = None
    window = None

    def __init__(self, frame):
        self.root = frame
        self.window = Toplevel(frame)
        self.set_window()

        self.button = Button(self.window, text="close", command=self.window.withdraw)
        self.button.place(x=530, y=350)

    def set_window(self):
        self.window.configure(bg="beige", bd=3, relief="ridge")
        self.window.title("통계")
        # self.window.overrideredirect(True)      # 윈도우창 상태표시줄 유무
        self.window.withdraw()                  # 윈도우 안 보이게

    def show_window(self):
        self.window.geometry(self.root.winfo_geometry())
        self.window.deiconify()


# test
if __name__ == "__main__":
    window = Tk()

    statistics_window = StatisticsGUI(window)

    button = Button(window, text="click me", command=statistics_window.window.deiconify)
    button.pack()

    window.mainloop()
