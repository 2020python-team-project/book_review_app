# -*- coding:utf-8 -*-
from urllib import parse
from book import Book
from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree
import pickle
from copy import *


class BookManager:
    ui = None
    books = []

    def __init__(self, ui):
        self.ui = ui
        self.load_from_file()
        # self.BooksDoc = self.LoadXMLFromFile()
        # self.get_book_info()

    def add_book(self, book):
        self.books.append(copy(book))
        self.ui.update_record_list()
        self.save_to_file()

    def save_to_file(self):
        print("책 저장할게")
        with open("book.pickle", "wb") as f:
            pickle.dump(self.books, f)

    def load_from_file(self):
        with open("book.pickle", "rb") as f:
            self.books = pickle.load(f)
        for book in self.books:
            book.print_info()


    # def LoadXMLFromFile(self):
    #     try:
    #         self.xmlFD = open("book.xml", encoding="UTF-8")  # xml 문서를 open합니다.
    #     except IOError:
    #         print("invalid file name or path")
    #         return None
    #     else:
    #         try:
    #             dom = parse(self.xmlFD)  # XML 문서를 파싱합니다.
    #         except Exception:
    #             print("loading fail!!!")
    #         else:
    #             print("XML Document loading complete")
    #             return dom
    #     return None
    #
    # def get_book_info(self):
    #     book = self.BooksDoc.getElementsByTagName("book")
    #     book_info = dict()
    #     for node in book:
    #         book_info["title"] = node.getElementsByTagName("title")[0].firstChild
    #         book_info["author"] = node.getElementsByTagName("author")[0].firstChild
    #
    #         for key, value in book_info.items():
    #             if value is None:
    #                 book_info[key] = ""
    #             else:
    #                 book_info[key] = value.data
    #
    #         recordedBooks = Book(
    #             title=book_info["title"],
    #             author=book_info["author"]
    #         )
    #         self.books.append(recordedBooks)
