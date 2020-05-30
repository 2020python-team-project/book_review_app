# -*- coding:utf-8 -*-

import http.client
from urllib import parse
from xml.dom import minidom
from book import Book

# urllib
# url과 관련된 패키지. url 파싱부터 url에 할당된 데이터를 수집하는 등 다양한 기능 제공

# DOM?
# 문서 객체 모델(Document Object Model)
# XML이나 HTML 문서에 접근하기 위한 표준임


option_to_varname = {
    "title": "d_titl=",
    "author": "d_auth=",
    "publisher": "d_publ="
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
    category = ""   # 카테고리 번호가 들어간 string

    params = ""

    response = None
    docm = ""

    books = []      # 받아온 책의 정보를 담은 Book 객체를 저장하는 리스트

    def __init__(self):
        self.conn = http.client.HTTPSConnection("openapi.naver.com")

        self.headers = {
            "X-Naver-Client-Id": self.client_id,
            "X-Naver-Client-Secret": self.client_secret
        }

    def set_search_word(self, word):
        self.search_word = parse.quote(word)    # encoding 된 텍스트

    def set_category(self, value=""):
        self.category = value

    def set_display_num(self, num=10):
        self.display_num = num

    def set_start_num(self, num=1):
        self.start_num = num

    def set_search_params(self, option):
        self.params = option_to_varname[option] + self.search_word \
                      + "&display=" + str(self.display_num) + "&start=" + str(self.start_num) \
                      + "&d_catg=" + self.category

    def request_search_result(self, option):
        self.set_search_params(option)
        self.conn.request("GET", "/v1/search/book_adv.xml?" + self.params, None, self.headers)
        self.response = self.conn.getresponse()

        if int(self.response.status) == 200:
            # 가져온 xml 파일의 정보를 Book 객체에 담는다.
            # 검색어에 <b> 검색어 </b> 이거 있음 해결해라
            self.docm = minidom.parseString(self.response.read().decode("utf-8"))
            titles = self.docm.getElementsByTagName("title")    # element 객체들의 리스트를 반환
            link = self.docm.getElementsByTagName("link")
            image = self.docm.getElementsByTagName("image")
            author = self.docm.getElementsByTagName("author")
            price = self.docm.getElementsByTagName("price")
            discount = self.docm.getElementsByTagName("discount")       # 이 정보 필요해?
            publisher = self.docm.getElementsByTagName("publisher")
            pubdate = self.docm.getElementsByTagName("pubdate")
            isbn = self.docm.getElementsByTagName("isbn")
            description = self.docm.getElementsByTagName("description")

            for i in range(self.display_num):
                book = Book(titles[i].firstChild.data, link[i].firstChild.data, image[i].firstChild.data,
                            author[i].firstChild.data, price[i].firstChild.data, discount[i].firstChild.data,
                            publisher[i].firstChild.data, pubdate[i].firstChild.data, isbn[i].firstChild.data,
                            description[i].firstChild.data)
                self.books.append(book)

            # 확인용 출력
            for book in self.books:
                book.print_info()

        else:
            print("HTTP Request is failed :" + self.response.reason)
            print(self.response.read().decode('utf-8'))

        self.conn.close()   # 언제 connection 닫아?


# 응답 예시
# < HTTP/1.1 200 OK
# < Server: nginx
# < Date: Mon, 26 Sep 2016 01:40:35 GMT
# < Content-Type: text/xml;charset=utf-8
# < Transfer-Encoding: chunked
# < Connection: keep-alive
# < Keep-Alive: timeout=5
# < Vary: Accept-Encoding
# < X-Powered-By: Naver
# < Cache-Control: no-cache, no-store, must-revalidate
# < Pragma: no-cache
# <
# <?xml version="1.0" encoding="UTF-8"?>
# <rss version="2.0">
#     <channel>
#         <title>Naver Open API - book ::'주식'</title>
#         <link>http://search.naver.com</link>
#         <description>Naver Search Result</description>
#         <lastBuildDate>Mon, 26 Sep 2016 10:40:35 +0900</lastBuildDate>
#         <total>20177</total><start>1</start><display>10</display>
#         <item>
#             <title>불곰의 <b>주식</b>투자 불패공식 (60개 매도종목 평균 수익률 62%)</title>
#             <link>http://openapi.naver.com/l?AAAC3LSwqDMBSF4dXcDCV6YxsHGfiog6JIV1A0SYloGpumQnffFIQz+DnwvT7afwVcaigRqvofvIKiIcbrhzAhbIAlZG3c5NySPMdd+0Q6exxqOuKudBjnNdlMFO00K8AmpRzZKackiJSdGc8ZxZzSglix3vqhG6KVKPcis0vXX+k+vqXM2BLpDzHjEYWYAAAA</link>
#             <image>http://bookthumb.phinf.naver.net/cover/108/346/10834650.jpg?type=m1&udate=20160902</image>
#             <author>불곰 박선목</author>
#             <price>16000</price>
#             <discount>14400</discount>
#             <publisher>부키</publisher>
#             <pubdate>20160729</pubdate>
#             <isbn>8960515523 9788960515529</isbn>
#             <description>잘못된 <b>주식</b>투자 습관을 버리고, 절대로 지지 않는 투자법을 체득하다!불곰<b>주식</b>연구소 대표 ‘불곰’이 알려 주는 세상에서 가장 쉬운 ‘<b>주식</b>투자 불패공식’ 『불곰의 <b>주식</b>투자 불패공식』. 불곰은 전업투자자가 아니다. 불곰<b>주식</b>연구소는 태평스럽게도 한 달에 한 종목 정도만 추천할 따름이다. 그럼에도... </description></item><item><title>엄마, <b>주식</b> 사주세요 (아이와 엄마의 미래를 위한 투자 원칙)</title><link>http://openapi.naver.com/l?AAACssTS2qtFV1dVZ1NFZ1cgYxLJxULV3UMopS02wzSkoKVI0dVY3cgCgpPz9bLy+xLLVILzk/FyqQkgRlxKekliRm5ugVZAB1uCVlpqgauxgamJsZmZlZqpXYGpqYm1iYmhgYmxoYWKrl2oaYpnokpmR6mhX6G1mkhHsDzXOqAGJDU8+M8rRIoGYA29JYJ5oAAAA=</link><image>http://bookthumb.phinf.naver.net/cover/107/626/10762669.jpg?type=m1&udate=20160802</image><author>존 리</author><price>14000</price><discount>12600</discount><publisher>한국경제신문사</publisher><pubdate>20160627</pubdate><isbn>8947541184 9788947541183</isbn><description>엄마의 <b>주식</b> 투자가 아이의 미래다!『엄마, <b>주식</b> 사주세요』는 전설의 펀드 투자자, 코리아펀드의 귀재로 불리며 새로운 마켓 리더로 부상한 존 리가... 저자는 이 책을 통해 자녀를 월급쟁이가 아닌 자본가로 키울 것과, <b>주식</b>투자에 대한 엄마들의 편견에 대해 중점적으로 이야기한다. 부를 축적하기 위한 자본가... </description>
#         </item>
#         ...
#     </channel>
# </rss>

if __name__ == "__main__":
    # test code
    search_engine = BookSearchEngine()
    search_engine.set_search_word("한강")
    search_engine.set_display_num()
    search_engine.set_start_num()

    search_engine.request_search_result("author")

