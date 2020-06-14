# 어차피 정보만 저장하는데 딕셔너리로 하는 게 이득인가...?
class Book:

    def __init__(self, title="", link="", image="", author="", price="",
                 publisher="", pubdate="",  description="",
                 comment="", date="", rating=""):
        self.title = title
        self.link = link
        self.image = image
        self.author = author
        self.price = price
        self.publisher = publisher
        self.pubdate = pubdate
        self.description = description

        self.user_comment = comment
        self.edit_date = date
        self.rating = rating

    def print_info(self):
        print(self.title)
        print(self.link)
        print(self.image)
        print(self.author)
        print(self.price)
        print(self.publisher)
        print(self.pubdate)
        print(self.description)
        print(self.user_comment)
        print(self.edit_date)
        print(str(self.rating))
        print("-" * 50)
