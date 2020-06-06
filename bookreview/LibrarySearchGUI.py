from tkinter import *
from tkinter import font

class LibrarySearchGUI:
    def __init__(self, frame):
        self.TempFont = font.Font(size=14, weight='bold', family='Consolas')
        self.detail_font = font.Font(size=10, family='Consolas')

        self.create_widget(frame)
        self.place_widget()

    def create_widget(self, frame):
        self.setting_frame = Frame(frame, bg="white", width=420, height=100)
        self.result_frame = Frame(frame, bg="white", width=420, height=330)

    def place_widget(self):
        # Place Widget
        self.setting_frame.place(x=250, y=10, anchor="n")
        self.result_frame.place(x=250, y=130, anchor="n")

