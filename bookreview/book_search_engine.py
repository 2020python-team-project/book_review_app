# -*- coding:utf-8 -*-
import http.client
from urllib import parse
from xml.dom import minidom


# urllib
# url과 관련된 패키지. url 파싱부터 url에 할당된 데이터를 수집하는 등 다양한 기능 제공

# DOM?
# 문서 객체 모델(Document Object Model)
# XML이나 HTML 문서에 접근하기 위한 표준임

option_to_varname = {
    "제목": "d_titl=",
    "저자": "d_auth=",
    "출판사": "d_publ="
}

catg_to_num = {
    "전체": "",
    "소설": "100",
    "시/에세이": "110",
    "인문": "120",
    "자기계발": "170",
    "역사/문화": "190",
    "해외도서": "340"
}


class BookSearchEngine:
    client_id = "zXYfFfpgUra2QxMwDRpk"
    client_secret = "orJlgTQcLV"

    conn = None
    headers = None

    # parameters
    search_word = ""
    display_num = int()
    start_num = int()
    catg_num = ""   # 카테고리 번호가 들어간 string

    params = ""

    response = None
    docm = ""

    search_total = int()
    searched_books = []      # 받아온 책의 정보를 담은 Book 객체를 저장하는 리스트

    def __init__(self):

        self.headers = {
            "X-Naver-Client-Id": self.client_id,
            "X-Naver-Client-Secret": self.client_secret
        }

    def set_search_word(self, word):
        self.search_word = parse.quote(word)    # encoding 된 텍스트

    def set_category(self, catg=""):
        self.catg_num = catg_to_num[catg]

    def set_display_num(self, num=30):
        self.display_num = num

    def set_start_num(self, num=1):
        self.start_num = num

    def _set_search_params(self, option):
        self.params = option_to_varname[option] + self.search_word \
                      + "&display=" + str(self.display_num) + "&start=" + str(self.start_num) \
                      + "&d_catg=" + self.catg_num

    def get_book_info(self):        # 가져온 xml 파일의 정보를 Book 객체에 담는다.
        self.docm = minidom.parseString(self.response.read().decode("utf-8"))

        # 검색 결과 수 가져오기
        total = self.docm.getElementsByTagName("total")  # NodeList
        self.search_total = int(total[0].firstChild.data)
        items = self.docm.getElementsByTagName("item")
        book_info = dict()  # { str: Text or None }

        for node in items:
            book_info["title"] = node.getElementsByTagName("title")[0].firstChild
            book_info["link"] = node.getElementsByTagName("link")[0].firstChild
            book_info["image"] = node.getElementsByTagName("image")[0].firstChild
            book_info["author"] = node.getElementsByTagName("author")[0].firstChild
            book_info["price"] = node.getElementsByTagName("price")[0].firstChild
            book_info["publisher"] = node.getElementsByTagName("publisher")[0].firstChild
            book_info["pubdate"] = node.getElementsByTagName("pubdate")[0].firstChild
            book_info["description"] = node.getElementsByTagName("description")[0].firstChild

            # Text 객체가 존재하는 지 검사
            for key, value in book_info.items():
                if value is None:
                    book_info[key] = ""
                else:
                    book_info[key] = value.data\
                        .replace("<b>", "").replace("</b>", "").replace("&#x0D;", "") # 불필요한 문자열 제거

            # book = Book(
            #     title=book_info["title"].replace("<b>", "").replace("</b>", ""),
            #     link=book_info["link"],
            #     image=book_info["image"],
            #     author=book_info["author"].replace("<b>", "").replace("</b>", ""),
            #     price=book_info["price"],
            #     publisher=book_info["publisher"].replace("<b>", "").replace("</b>", ""),
            #     pubdate=book_info["pubdate"],
            #     description=book_info["description"].replace("<b>", "").replace("</b>", "") .replace("&#x0D;", "")
            # )
            self.searched_books.append(book_info.copy())

        # 확인용 출력
        # for book in self.books:
        #     book.print_info()

    def request_search_result(self, option):
        self.searched_books.clear()  # 객체까지 모두 삭제되니?
        self.conn = http.client.HTTPSConnection("openapi.naver.com")
        self._set_search_params(option)
        # 만약 네트워크가 연결되어 있지 않으면 에러 남. 해결해야하나....ㅠ
        self.conn.request("GET", "/v1/search/book_adv.xml?" + self.params, None, self.headers)
        self.response = self.conn.getresponse()

        if int(self.response.status) == 200:
            self.get_book_info()
        else:
            print("HTTP Request is failed :" + self.response.reason)
            print(self.response.read().decode('utf-8'))

        self.conn.close()

    def get_total(self):
        return self.search_total


if __name__ == "__main__":
    # test code
    search_engine = BookSearchEngine()
    search_engine.set_search_word("대화")
    search_engine.set_display_num()
    search_engine.set_start_num()

    search_engine.request_search_result("제목")

