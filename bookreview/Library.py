class Library:
    def __init__(self, SIGUN_NM="", EMD_NM="", LIBRRY_NM="", HMPG_ADDR="",
                 REFINE_ROADNM_ADDR="", READROOM_OPEN_TM_INFO="",  READROOM_REST_DE_INFO=""):
        self.SIGUN_NM = SIGUN_NM
        self.EMD_NM = EMD_NM
        self.LIBRRY_NM = LIBRRY_NM
        self.HMPG_ADDR = HMPG_ADDR
        self.REFINE_ROADNM_ADDR = REFINE_ROADNM_ADDR
        self.READROOM_OPEN_TM_INFO = READROOM_OPEN_TM_INFO
        self.READROOM_REST_DE_INFO = READROOM_REST_DE_INFO

    def print_info(self):
        print(self.SIGUN_NM)
        print(self.EMD_NM)
        print(self.LIBRRY_NM)
        print(self.HMPG_ADDR)

        print("-" * 50)



