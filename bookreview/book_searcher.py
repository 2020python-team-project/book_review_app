# -*- coding:utf-8 -*-

import http.client
from urllib import parse
from xml.dom.minidom import parseString

# urllib
# url과 관련된 패키지. url 파싱부터 url에 할당된 데이터를 수집하는 등 다양한 기능 제공

# DOM?
# 문서 객체 모델(Document Object Model)
# XML이나 HTML 문서에 접근하기 위한 표준임

# 이거 클래스로 잘 구성하기

client_id = "zXYfFfpgUra2QxMwDRpk"
client_secret = "orJlgTQcLV"

conn = http.client.HTTPSConnection("openapi.naver.com")

headers = {
    "X-Naver-Client-Id": client_id,
    "X-Naver-Client-Secret": client_secret
}

search_keyword = input("검색어를 입력하세요: ")

encText = parse.quote(search_keyword)
display_num = 10                # 몇개의 정보를 가져올 지 정할 수 있음
start_num = 1                   # 정보의 시작 위치를 정할 수 있음
params = "?query=" + encText + "&display=" + str(display_num) + "&start=" + str(start_num)

conn.request("GET", "/v1/search/book.xml" + params, None, headers)  # 정보를 요청하고
res = conn.getresponse()                                            # 받아옴

if int(res.status) == 200:      # 200은 성공 응답 코드, 더 알고 싶으면 http 상태 코드 검색
    print(parseString(res.read().decode('utf-8')).toprettyxml())
    # Node.toprettyxml() -> 문서의 예쁘게 인쇄된 버전을 반환합니다...
    # 가져왔다면 문서를 파싱해서 알맞은 자리에 데이터를 넣는 방법을 찾아보면 되겠네
else:
    print("HTTP Request is failed :" + res.reason)
    print(res.read().decode('utf-8'))

conn.close()
