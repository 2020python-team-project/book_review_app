# -*- coding:utf-8 -*-
import http.client
from urllib import parse
from xml.dom.minidom import *
import urllib.request



class BestsellerSearchEngine:
    resp = None
    category=100
    params=""

    searched_books = []
    docm = ""

    myServerKey = "C11CC57608240722FEF373CCAC58307E1847C34E6C90024CE192B678B275E0AB"
    url = "http://book.interpark.com/api/bestSeller.api?"

    def __init__(self):
        self.set_search()

    def set_search(self):
        self.searched_books.clear()
        self.params="key=" + self.myServerKey + "&categoryId="+str(self.category)+"&output=xml"

        self.serverurl=self.url+self.params
        self.get_Book()



    def get_Book(self):
        req = urllib.request.Request(self.serverurl)
        try:
            self.resp = urllib.request.urlopen(req)
        except urllib.error.URLError as e:
            print(e.reason)
            print(parseString(e.read().decode('utf-8')).toprettyxml())
        except urllib.error.HTTPError as e:
            print("error code=" + e.code)
            print(parseString(e.read().decode('utf-8')).toprettyxml())
        else:
            self.docm= parseString(self.resp.read().decode('utf-8'))
            print("&"*50+self.docm.toprettyxml())

        items = self.docm.getElementsByTagName("item")
        book_info = dict()

        for node in items:
            book_info["title"] = node.getElementsByTagName("title")[0].firstChild
            book_info["image"] = node.getElementsByTagName("coverSmallUrl")[0].firstChild
            book_info["author"] = node.getElementsByTagName("author")[0].firstChild
            book_info["price"] = node.getElementsByTagName("priceStandard")[0].firstChild
            book_info["publisher"] = node.getElementsByTagName("publisher")[0].firstChild
            book_info["pubDate"] = node.getElementsByTagName("pubDate")[0].firstChild
            book_info["description"] = node.getElementsByTagName("description")[0].firstChild
            book_info["isbn"] = node.getElementsByTagName("isbn")[0].firstChild

            # Text 객체가 존재하는 지 검사
            for key, value in book_info.items():
                if value is None:
                    book_info[key] = ""
                else:
                    book_info[key] = value.data \
                        .replace("<b>", "").replace("</b>", "").replace("&#x0D;", "")  # 불필요한 문자열 제거

        self.searched_books.append(book_info.copy())



    def urlencode(self,string):
        # URL 인코딩
        return urllib.parse.quote(string)


BestsellerSearchEngine()







