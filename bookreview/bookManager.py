# -*- coding:utf-8 -*-
from urllib import parse
from book import Book
from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree
import pickle
from copy import *


class BookManager:
    file_name = "book.pickle"
    ui = None
    books = []

    def __init__(self, ui):
        self.ui = ui
        self.load_from_file()

    def add_book(self, book):
        self.books.append(copy(book))
        self.ui.update_record_list()

        with open(self.file_name, "ab") as f:
            pickle.dump(book, f)

    def load_from_file(self):
        try:
            f = open(self.file_name, "rb")
        except IOError:
            print("데이터 없음!")
        else:
            while True:
                try:
                    book = pickle.load(f)
                except EOFError:
                    break
                else:
                    self.books.append(book)
