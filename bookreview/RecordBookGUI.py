# -*- coding: cp949 -*-
from tkinter import *
from tkinter import font
from recordDetailGUI import RecordDetailGUI
from BestsellerGUI import BestsellerGUI
import mimetypes
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import urllib.request
from xml.dom.minidom import getDOMImplementation
from datetime import date, datetime, timedelta


class RecordBookGUI:
    record_frame = None
    detail_frame = None

    plus_button = None
    minus_button = None
    statistic_button = None
    bestseller_button=None

    record_listbox = None
    record_scrollbar = None

    # detail
    detail_gui = None

    statistic_gui = None
    bestseller_gui = None

    book_manager = None

    def __init__(self, frame, book_manager):
        self.TempFont = font.Font(size=14, weight='bold', family='메이플스토리')
        self.small_font = font.Font(size=11, family='메이플스토리')

        self.book_manager = book_manager

        self.create_widget(frame)
        self.place_widget()
        self.update_record_list()

    def create_widget(self, frame):
        self.record_frame = Frame(frame, bg="white", width=420, height=330)

        self.email_button = Button(frame, text="이메일 전송", width=12, height=1, font=self.TempFont,
                                  command=self.sendEmail,bg='tan')
        self.email_entry=Entry(frame, relief="solid", font=self.TempFont, width=17)
        self.statistic_button = Button(frame, text="주간 통계보기", width=14, height=1, font=self.TempFont, bg='plum3')
        self.bestseller_button = Button(frame, text="오늘의 베스트셀러", width=14, height=1, font=self.TempFont, bg='pink')

        self.record_scrollbar = Scrollbar(self.record_frame)
        self.record_listbox = Listbox(self.record_frame, font=self.TempFont, width=30, height=15, activestyle="none",
                                      selectmode="single", yscrollcommand=self.record_scrollbar.set)

        self.record_listbox.bind("<Double-Button-1>", self.show_detail)

        self.detail_gui = RecordDetailGUI(frame, 250, 10)

    def place_widget(self):
        self.record_frame.place(x=250, y=130, anchor="n")

        self.email_button.place(x=275, y=75)
        self.email_entry.place(x=40,y=80)
        self.statistic_button.place(x=40, y=20)
        self.bestseller_button.place(x=250,y=20)

        self.record_listbox.pack(side="left")
        self.record_scrollbar.pack(side="right", fill='y')

    def update_record_list(self):
        self.record_listbox.delete(0, self.record_listbox.size())       # 원래 리스트 박스에 있던거 모두 삭제
        for i, book in enumerate(self.book_manager.books):
            self.record_listbox.insert(i, book.title)

    def show_detail(self, event):
        selected_index = self.record_listbox.curselection()
        if selected_index == ():
            return
        selected_book = self.book_manager.books[selected_index[0]]

        self.detail_gui.open(selected_book)

    def set_statistics_gui(self, gui):
        self.statistic_gui = gui
        self.statistic_button.configure(command=self.statistic_gui.show_window)

    def set_bestseller_gui(self, gui):
        self.Bestseller_gui = gui
        self.bestseller_button.configure(command=self.Bestseller_gui.show_window)

    def sendEmail(self):
        host = "smtp.gmail.com"  # Gmail STMP 서버 주소.
        port = "587"
        htmlFile=self.MakeHtmlDoc() #예쁘게 보내주려고 html 파일로 변환
        print(htmlFile)
        senderAddr = "ghdtmdgp12@gmail.com"  # 보내는 사람 email 주소.
        recipientAddr = urllib.parse.quote(self.email_entry.get()).replace("%40","@")    # 받는 사람 email 주소.

        msg = MIMEBase("multipart", "alternative")
        msg['Subject'] = "["+str(date.today())+"] 현재까지 읽은 책 목록 ♨"
        msg['From'] = senderAddr
        msg['To'] = recipientAddr

        # MIME 문서를 생성합니다.
        HtmlPart = MIMEText(htmlFile,'html', _charset='UTF-8')

        # 만들었던 mime을 MIMEBase에 첨부 시킨다.
        msg.attach(HtmlPart)

        # 메일을 발송한다.
        s = smtplib.SMTP(host, port)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login("ghdtmdgp12@gmail.com", "ghd5683734")
        s.sendmail(senderAddr, [recipientAddr], msg.as_string())
        s.close()

    def MakeHtmlDoc(self):
        # DOM 개체를 생성
        impl = getDOMImplementation()

        newdoc = impl.createDocument(None, "html", None)  # HTML 최상위 엘리먼트 생성
        top_element = newdoc.documentElement
        header = newdoc.createElement('header')
        top_element.appendChild(header)

        # Body 엘리먼트 생성
        body = newdoc.createElement('body')

        for i,bookitem in enumerate(self.book_manager.books):
            b = newdoc.createElement('b')  # Bold 엘리먼트 생성
            titleText = newdoc.createTextNode("제목:" + bookitem.title)  # 텍스트 노드 생성
            b.appendChild(titleText)

            br = newdoc.createElement('br')  # <br> 부분을 생성
            body.appendChild(br)

            a = newdoc.createElement('a')
            authorText = newdoc.createTextNode("->저자:" + bookitem.author)
            a.appendChild(authorText)

            p = newdoc.createElement('p')
            publisherText = newdoc.createTextNode("출판사:" + bookitem.publisher)
            p.appendChild(publisherText)

            #이미지가 안띄워짐 ㅠㅠ
            # image = newdoc.createTextNode(bookitem.image)  # 텍스트 노드 생성
            # img = newdoc.createElement('img src='+str(image))  # title 부분을 생성

            #body.appendChild(img)
            body.appendChild(b)
            body.appendChild(a)
            body.appendChild(p)
            body.appendChild(br)

        top_element.appendChild(body)  # Body 엘리먼트를 최상위 엘리먼트에 추가
        print(newdoc.toxml())
        return newdoc.toxml()

    def checkDocument(self):
        if self.book_manager.BooksDoc == None:
            print("Error : Document is empty")
            return False
        return True

