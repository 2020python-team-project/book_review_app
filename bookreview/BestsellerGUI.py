from tkinter import *
from tkinter import ttk
from tkinter import font


class BestsellerGUI:
    root = None
    window = None

    def __init__(self, frame):
        self.root = frame
        self.window = Toplevel(frame)
        self.set_window()

        self.button = Button(self.window, text="으앗차", command=self.window.withdraw)
        self.button.place(x=530, y=350)

    def set_window(self):
        self.window.configure(bg="beige", bd=3, relief="ridge")
        self.window.title("베스트셀러")
        # self.window.overrideredirect(True)      # 윈도우창 상태표시줄 유무
        self.window.withdraw()                  # 윈도우 안 보이게

    def show_window(self):
        self.window.geometry(self.root.winfo_geometry())
        self.window.deiconify()


# test
if __name__ == "__main__":
    window = Tk()

    statistics_window = BestsellerGUI(window)

    button = Button(window, text="click me", command=statistics_window.window.deiconify)
    button.pack()

    window.mainloop()
