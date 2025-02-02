class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
    def display_details(self):
        print(f"Title of the book: {self.title}")
        print(f"Author of the book: {self.author}")
        print(f"ISBN of the book: {self.isbn}")
title=input("Enter the title of the book:")
author=input("Enter the author of the book:")
isbn=input("enter the isbn of the book:")
b=Book(title,author,isbn)
b.display_details()
        