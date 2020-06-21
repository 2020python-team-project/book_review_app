import pickle
from copy import copy


class BookManager:
    file_name = "book.pickle"
    ui = None
    books = []

    def __init__(self):
        self.load_from_file()
        self.books = sorted(self.books, key=lambda bk: bk.edit_date, reverse=True)

    def set_record_ui(self, ui):
        self.ui = ui

    def add_book(self, book):
        self.books.append(copy(book))
        self.books = sorted(self.books, key=lambda bk: bk.edit_date, reverse=True)

        self.ui.update_record_list()

        with open(self.file_name, "ab") as f:
            pickle.dump(book, f)

    def remove_book(self, book):
        self.books.remove(book)
        self.save_books()

        self.ui.update_record_list()

    def save_books(self):
        # books에 있는 내용을 처음부터 다시 씀
        with open(self.file_name, "wb") as f:
            for book in self.books:
                pickle.dump(book, f)

    def load_from_file(self):
        try:
            f = open(self.file_name, "rb")
        except IOError:
            print("데이터 없음!")
        else:
            while True:
                try:
                    book = pickle.load(f)
                except EOFError:
                    break
                else:
                    self.books.append(book)
