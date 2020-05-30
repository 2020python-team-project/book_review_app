class Book:
    def __init__(self, title, link, image, author, price, discount, publisher, pubdate, isbn, description):
        self.title = title
        self.link = link
        self.image = image
        self.author = author
        self.price = price
        self.discount = discount
        self.publisher = publisher
        self.pubdate = pubdate
        self.isbn = isbn
        self.description = description

    def print_info(self):
        print(self.title)
        print(self.link)
        print(self.image)
        print(self.author)
        print(self.price)
        print(self.discount)
        print(self.publisher)
        print(self.pubdate)
        print(self.isbn)
        print(self.description)
        print("-" * 50)
