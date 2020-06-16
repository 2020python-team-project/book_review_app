from tkinter import *
from tkinter import font
from Library_search_engin import LibrarySearchEngine
import folium
import webbrowser

class LibrarySearchGUI:
    setting_frame = None
    result_frame = None
    detail_frame = None

    # setting frame
    library_search_button = None
    citykeyword_entry = None
    dongkeyword_entry = None

    first_label=None
    second_label=None

    # result frame
    result_listbox = None
    result_scrollbar = None

    # detail frame
    name_label = None
    hompage_label = None
    adress_label = None
    openTime_label = None
    restDay_label = None
    back_to_list_button = None

    Lsrch_engine=None


    def __init__(self, frame):
        self.TempFont = font.Font(size=14, weight='bold', family='메이플스토리')
        self.big_font = font.Font(size=25, weight='bold', family='메이플스토리')

        self.create_widget(frame)
        self.place_widget()

        self.Lsrch_engine= LibrarySearchEngine()

    def create_widget(self, frame):
        self.setting_frame = Frame(frame, bg="white", width=420, height=100)
        self.detail_frame = Frame(frame, bg="white", width=420, height=335)
        self.result_frame = Frame(frame, bg="white", width=420, height=330)

        self.citykeyword_entry = Entry(self.setting_frame, relief="solid", font=self.TempFont, width=15)
        self.dongkeyword_entry = Entry(self.setting_frame, relief="solid", font=self.TempFont, width=15)
        self.library_search_button = Button(self.setting_frame, text="검색", font=self.TempFont, bg='indian red',
                                            command=self.search_library, width=4, height=2)
        self.citykeyword_entry.bind("<Return>", self.search_library)
        self.dongkeyword_entry.bind("<Return>", self.search_library)

        self.first_label=Label(self.setting_frame,font=self.TempFont,bg="white",text="시/도 명:")
        self.second_label = Label(self.setting_frame, font=self.TempFont, bg="white", text="읍/면/동 명 :")

        #result
        self.result_scrollbar = Scrollbar(self.result_frame)
        self.result_listbox = Listbox(self.result_frame, font=self.TempFont, width=30, height=15, activestyle="none",
                                      selectmode="single", yscrollcommand=self.result_scrollbar.set)

        self.result_listbox.bind("<Double-Button-1>", self.show_detail)

        #detail
        self.name_label=Label(self.detail_frame,font=self.big_font,bg='white')
        self.adress_label=Label(self.detail_frame,font=self.TempFont,text="주소: ",bg='white')
        self.openTime_label=Label(self.detail_frame,font=self.TempFont,text="운영시간: ",bg='white')
        self.restDay_label=Label(self.detail_frame,font=self.TempFont,text="휴관일: ",bg='white')
        self.hompage_label=Label(self.detail_frame,font=self.TempFont,text="홈페이지: ",bg='white')

        self.back_to_list_button = Button(self.detail_frame, font=self.TempFont, text="목록으로",
                                          command=self.detail_frame.place_forget)

        self.map_button = Button(self.detail_frame, font=self.TempFont, text="지도보기",
                                          command=self.show_map)


    def place_widget(self):
        # Place Widget
        self.setting_frame.place(x=250, y=10, anchor="n")
        self.result_frame.place(x=250, y=130, anchor="n")

        self.citykeyword_entry.place(x=130, y=30, anchor="w")
        self.dongkeyword_entry.place(x=130, y=70, anchor="w")
        self.library_search_button.place(x=340, y=50, anchor="w")
        self.first_label.place(x=20, y=30, anchor="w")
        self.second_label.place(x=20, y=70, anchor="w")

        self.result_listbox.pack(side="left")
        self.result_scrollbar.pack(side="right", fill='y')

        self.name_label.place(x=10,y=10)
        self.adress_label.place(x=10,y=70)
        self.openTime_label.place(x=10,y=100)
        self.restDay_label.place(x=10,y=130)
        self.hompage_label.place(x=10,y=160)

        self.back_to_list_button.place(x=10, y=300, anchor="w")
        self.map_button.place(x=330,y=300, anchor="w")


    def search_library(self, event=None):
        self.Lsrch_engine.search_city=\
            self.Lsrch_engine.urlencode(self.citykeyword_entry.get())
        self.Lsrch_engine.search_dong = \
            self.Lsrch_engine.urlencode(self.dongkeyword_entry.get())
        self.Lsrch_engine.set_search()

        self.result_listbox.delete(0, self.result_listbox.size())
        for i, lib in enumerate(self.Lsrch_engine.library_list):
            self.result_listbox.insert(i, lib.LIBRRY_NM)

        self.detail_frame.place_forget()    # detail창이 띄워진 상태일 수도 있으니 닫는다.


    def show_detail(self,event):
        self.selected_index = self.result_listbox.curselection()
        if self.selected_index == ():
            return

        self.selected = self.Lsrch_engine.library_list[self.selected_index[0]]

        self.name_label["text"]=" 『"+selected.LIBRRY_NM+"』 "
        self.adress_label["text"]="주소: "+selected.LIBRRY_NM
        self.openTime_label["text"]="영업시간: "+selected.READROOM_OPEN_TM_INFO
        self.restDay_label["text"]="휴관일: "+selected.READROOM_REST_DE_INFO
        self.hompage_label["text"]="홈페이지: "+selected.HMPG_ADDR

        self.detail_frame.place(x=250, y=130, anchor="n")

    def show_map(self):
        # 위도 경도 지정
        map_osm = folium.Map(location=[float(self.selected.REFINE_WGS84_LAT), float(self.selected.REFINE_WGS84_LOGT)], zoom_start=15)
        # 마커 지정
        folium.Marker([float(self.selected.REFINE_WGS84_LAT), float(self.selected.REFINE_WGS84_LOGT)], popup='한국산업기술대').add_to(map_osm)
        # html 파일로 저장
        map_osm.save('osm.html')
        webbrowser.open_new('osm.html')