from tkinter import *
from tkinter import font
import tkinter.messagebox

class MainGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("♥ 나만의 독서기록장 ♥")
        self.window.geometry("1000x600+200+100")
        self.TempFont = font.Font(size=16, weight='bold', family='Consolas')
        self.window.configure(bg="beige")
        self.InitTopText()
        self.B1 = Button(self.window, text="책 검색", width=8, height=1, font=self.TempFont)
        self.B1.place(x=50, y=70)
        self.B2 = Button(self.window, text="도서관 찾기", width=10, height=1, font=self.TempFont)
        self.B2.place(x=200, y=70)

        self.B3 = Button(self.window, text="+", width=2, height=1, font=self.TempFont)
        self.B3.place(x=880, y=180)
        self.B4 = Button(self.window, text="-", width=2, height=1, font=self.TempFont)
        self.B4.place(x=920, y=180)

        self.B5 = Button(self.window, text="주간 통계보기", width=10, height=1, font=self.TempFont)
        self.B5.place(x=530, y=180)

        self.Booksearch()
        self.Bookresult()
        self.Myrecord()
        self.window.mainloop()

    def InitTopText(self):
        Font = font.Font(self.window, size=25, weight='bold', family='Consolas')
        MainText = Label(self.window, font=Font, text="♥ 나만의 독서기록장 ♥")
        MainText.pack()
        MainText.place(x=60, y=10)

    def Booksearch(self):
        self.canvas = Canvas(self.window, bg="white", width=420, height=100)
        self.canvas.pack()
        self.canvas.place(x=30, y=120)
        self.Font2 = font.Font(size=15, weight='bold', family='Consolas')
        Label(text="제목", font=self.Font2).place(x=40, y=130)
        Entry().place(x=85, y=135)
        Label(text="저자", font=self.Font2).place(x=40, y=180)
        Entry().place(x=85, y=185)
        Label(text="출판사", font=self.Font2).place(x=230, y=130)
        Entry().place(x=295, y=135)
        Label(text="장르", font=self.Font2).place(x=230, y=180)
        Radiobutton(text="소설",value=1).place(x=295,y=185)

    def Bookresult(self):
        self.canvas = Canvas(self.window, bg="white", width=420, height=330)
        self.canvas.pack()
        self.canvas.place(x=30, y=230)
        self.Font = font.Font(size=15, weight='bold', family='Consolas')

    def Myrecord(self):
        self.canvas = Canvas(self.window, bg="white", width=420, height=330)
        self.canvas.pack()
        self.canvas.place(x=530, y=230)
        self.Font = font.Font(size=15, weight='bold', family='Consolas')

MainGUI()

