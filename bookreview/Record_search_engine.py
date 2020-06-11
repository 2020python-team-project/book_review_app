# -*- coding:utf-8 -*-
import http.client
from urllib import parse
from book import Book
from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree

class RecordSearchEngine:
    xmlFD = -1
    books=[]

    def __init__(self):
        self.BooksDoc=self.LoadXMLFromFile()
        self.get_book_info()

    def LoadXMLFromFile(self):

        try:
            self.xmlFD = open("book.xml",encoding="UTF-8")  # xml 문서를 open합니다.
        except IOError:
            print("invalid file name or path")
            return None
        else:
            try:
                dom = parse(self.xmlFD)  # XML 문서를 파싱합니다.
            except Exception:
                print("loading fail!!!")
            else:
                print("XML Document loading complete")
                return dom
        return None

    def get_book_info(self):
        book= self.BooksDoc.getElementsByTagName("book")
        book_info = dict()
        for node in book:
            book_info["title"] = node.getElementsByTagName("title")[0].firstChild
            book_info["author"] = node.getElementsByTagName("author")[0].firstChild

            for key, value in book_info.items():
                if value is None:
                    book_info[key] = ""
                else:
                    book_info[key] = value.data

            recordedBooks = Book(
                title=book_info["title"],
                author=book_info["author"]
            )
            self.books.append(recordedBooks)
