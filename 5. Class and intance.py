import math


class Book:
    fontSize = 12
    pageWidth = 17

    def __init__(self, title, writer, year, length, price):
        self.title = title
        self.writer = writer
        self.year = year
        self.length = length
        self.price = price

    def number_of_pages(self):
        pages = (self.length * self.fontSize) / (self.pageWidth * 100)
        return math.ceil(pages)

    def bookInformation(self):
        return "Title : {} \nwriter : {}\nbook publish : {}\nprice : Rp.{}\nnumber of pages : {} pages" \
            .format(self.title, self.writer, self.year, self.price, self.number_of_pages())


newBook1 = Book("Fundamental Data of Science", "Debb", "2022", 5000, 150000)
# print(newBook1.title)
# print(newBook1.writer)
# print(newBook1.number_of_pages())
print(newBook1.bookInformation())