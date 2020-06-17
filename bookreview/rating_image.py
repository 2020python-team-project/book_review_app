from tkinter import PhotoImage

default = None
good = None
normal = None
bad = None


def load_image():
    global default, good, normal, bad
    default = PhotoImage(file="Resource/Image/rating_default.PNG")
    good = PhotoImage(file="Resource/Image/rating_good.PNG")
    normal = PhotoImage(file="Resource/Image/rating_normal.PNG")
    bad = PhotoImage(file="Resource/Image/rating_bad.PNG")


def get_rating_image(rating):
    if rating == 0:
        return default
    elif rating == 1:
        return bad
    elif rating == 2:
        return normal
    else:
        return good
