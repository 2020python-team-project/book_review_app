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
        self.TempFont = font.Font(size=14, weight='bold', family='�����ý��丮')
        self.small_font = font.Font(size=11, family='�����ý��丮')

        self.book_manager = book_manager

        self.create_widget(frame)
        self.place_widget()
        self.update_record_list()

    def create_widget(self, frame):
        self.record_frame = Frame(frame, bg="white", width=420, height=330)

        self.email_button = Button(frame, text="�̸��� ����", width=12, height=1, font=self.TempFont,
                                  command=self.sendEmail,bg='tan')
        self.email_entry=Entry(frame, relief="solid", font=self.TempFont, width=17)
        self.statistic_button = Button(frame, text="�ְ� ��躸��", width=14, height=1, font=self.TempFont, bg='plum3')
        self.bestseller_button = Button(frame, text="������ ����Ʈ����", width=14, height=1, font=self.TempFont, bg='pink')

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
        self.record_listbox.delete(0, self.record_listbox.size())       # ���� ����Ʈ �ڽ��� �ִ��� ��� ����
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
        host = "smtp.gmail.com"  # Gmail STMP ���� �ּ�.
        port = "587"
        htmlFile=self.MakeHtmlDoc() #���ڰ� �����ַ��� html ���Ϸ� ��ȯ
        print(htmlFile)
        senderAddr = "ghdtmdgp12@gmail.com"  # ������ ��� email �ּ�.
        recipientAddr = urllib.parse.quote(self.email_entry.get()).replace("%40","@")    # �޴� ��� email �ּ�.

        msg = MIMEBase("multipart", "alternative")
        msg['Subject'] = "["+str(date.today())+"] ������� ���� å ��� ��"
        msg['From'] = senderAddr
        msg['To'] = recipientAddr

        # MIME ������ �����մϴ�.
        HtmlPart = MIMEText(htmlFile,'html', _charset='UTF-8')

        # ������� mime�� MIMEBase�� ÷�� ��Ų��.
        msg.attach(HtmlPart)

        # ������ �߼��Ѵ�.
        s = smtplib.SMTP(host, port)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login("ghdtmdgp12@gmail.com", "ghd5683734")
        s.sendmail(senderAddr, [recipientAddr], msg.as_string())
        s.close()

    def MakeHtmlDoc(self):
        # DOM ��ü�� ����
        impl = getDOMImplementation()

        newdoc = impl.createDocument(None, "html", None)  # HTML �ֻ��� ������Ʈ ����
        top_element = newdoc.documentElement
        header = newdoc.createElement('header')
        top_element.appendChild(header)

        # Body ������Ʈ ����
        body = newdoc.createElement('body')

        for i,bookitem in enumerate(self.book_manager.books):
            b = newdoc.createElement('b')  # Bold ������Ʈ ����
            titleText = newdoc.createTextNode("����:" + bookitem.title)  # �ؽ�Ʈ ��� ����
            b.appendChild(titleText)

            br = newdoc.createElement('br')  # <br> �κ��� ����
            body.appendChild(br)

            a = newdoc.createElement('a')
            authorText = newdoc.createTextNode("->����:" + bookitem.author)
            a.appendChild(authorText)

            p = newdoc.createElement('p')
            publisherText = newdoc.createTextNode("���ǻ�:" + bookitem.publisher)
            p.appendChild(publisherText)

            #�̹����� �ȶ���� �Ф�
            # image = newdoc.createTextNode(bookitem.image)  # �ؽ�Ʈ ��� ����
            # img = newdoc.createElement('img src='+str(image))  # title �κ��� ����

            #body.appendChild(img)
            body.appendChild(b)
            body.appendChild(a)
            body.appendChild(p)
            body.appendChild(br)

        top_element.appendChild(body)  # Body ������Ʈ�� �ֻ��� ������Ʈ�� �߰�
        print(newdoc.toxml())
        return newdoc.toxml()

    def checkDocument(self):
        if self.book_manager.BooksDoc == None:
            print("Error : Document is empty")
            return False
        return True

