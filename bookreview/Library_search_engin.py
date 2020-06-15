# -*- coding:utf-8 -*-
import http.client
from urllib import parse
from xml.dom.minidom import *
import urllib.request
from Library import Library



class LibrarySearchEngine:
    resp = None
    library_list=[]
    search_city=""
    search_dong = ""
    params=""

    myServerKey = "478ea3e12cdb44d69077fb4916bce277"
    url = "https://openapi.gg.go.kr/Tbggibllbrm?"


    def set_search(self):
        self.library_list.clear()
        self.params="KEY=" + self.myServerKey + "&Type=xml&pIndex=1&pSize=50&SIGUN_NM=" + self.search_city \
                    +"&EMD_NM="+self.search_dong

        self.serverurl=self.url+self.params
        self.get_Library()

    def get_Library(self):
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
            #print("&"*50+self.docm.toprettyxml())
            #toprettyxml는 xml 형식으로 바꿔주는 함수

        row = self.docm.getElementsByTagName("row")
        library_info = dict()

        for node in row:
            library_info["SIGUN_NM"] = node.getElementsByTagName("SIGUN_NM")[0].firstChild
            library_info["EMD_NM"] = node.getElementsByTagName("EMD_NM")[0].firstChild
            library_info["LIBRRY_NM"] = node.getElementsByTagName("LIBRRY_NM")[0].firstChild
            library_info["HMPG_ADDR"] = node.getElementsByTagName("HMPG_ADDR")[0].firstChild
            library_info["REFINE_ROADNM_ADDR"] = node.getElementsByTagName("REFINE_ROADNM_ADDR")[0].firstChild
            library_info["READROOM_OPEN_TM_INFO"] = node.getElementsByTagName("READROOM_OPEN_TM_INFO")[0].firstChild
            library_info["READROOM_REST_DE_INFO"] = node.getElementsByTagName("READROOM_REST_DE_INFO")[0].firstChild
            library_info["REFINE_WGS84_LAT"] = node.getElementsByTagName("REFINE_WGS84_LAT")[0].firstChild
            library_info["REFINE_WGS84_LOGT"] = node.getElementsByTagName("REFINE_WGS84_LOGT")[0].firstChild
            for key, value in library_info.items():
                if value is None:
                    library_info[key] = ""
                else:
                    library_info[key] = value.data

            library = Library(
                SIGUN_NM=library_info["SIGUN_NM"],
                EMD_NM=library_info["EMD_NM"],
                LIBRRY_NM=library_info["LIBRRY_NM"],
                HMPG_ADDR=library_info["HMPG_ADDR"],
                REFINE_ROADNM_ADDR=library_info["HMPG_ADDR"],
                READROOM_OPEN_TM_INFO=library_info["REFINE_ROADNM_ADDR"],
                READROOM_REST_DE_INFO=library_info["READROOM_REST_DE_INFO"],
                REFINE_WGS84_LAT=library_info["REFINE_WGS84_LAT"],
                REFINE_WGS84_LOGT=library_info["REFINE_WGS84_LOGT"]
            )
            self.library_list.append(library)

            # for i in self.library_list:
            #     i.print_info()

    def urlencode(self,string):
        # URL 인코딩
        return urllib.parse.quote(string)


LibrarySearchEngine()







