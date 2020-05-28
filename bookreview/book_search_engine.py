# -*- coding:utf-8 -*-

import http.client
from urllib import parse
from xml.dom.minidom import parseString

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
    result = ""

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
            self.result = parseString(self.response.read().decode("utf-8")).toprettyxml()
            print(self.result)
            # 이 정보를 가져왔으면 Book의 객체를 생성하고 어딘가 저장
            # 어떻게 생성하고 어디 저장함ㅠ
        else:
            print("HTTP Request is failed :" + self.response.reason)
            print(self.response.read().decode('utf-8'))

        self.conn.close()   # 언제 connection 닫아?


if __name__ == "__main__":
    # test code
    search_engine = BookSearchEngine()
    search_engine.set_search_word("대화")
    search_engine.set_display_num()
    search_engine.set_start_num()

    search_engine.request_search_result("title")

