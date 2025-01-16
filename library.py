class Library:
    def __init__(self):
        self.__books = []
    def add_books(self,book):
        self.__books.append(book)
    def show_books(self):
        for book in self.__books:
            if isinstance(book, DigitalBook):
                print(book.show_digital_book_details())
            elif isinstance(book, AudioBook):
                print(book.show_audiobook_details())
            else:
                print(book.get_book_details())
            print('------------------------------------------------------------------------------------------')

class Book:
    def __init__(self, title, author, pages, ISBN, price):
        self.title = title 
        self.author = author
        self.pages = pages
        self.__ISBN = ISBN
        self.__price = price

    def get_book_details(self):

        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, ISBN: {self.__ISBN}, Price: {self.__price}"
    

class DigitalBook(Book):
    def __init__(self, title, author, pages, ISBN, price, filesize):
        super().__init__(title, author, pages, ISBN, price)
        self.filesize = filesize

    def show_digital_book_details(self):
        return f"{super().get_book_details()}, Filesize: {self.filesize} MB"
    
class AudioBook(Book):
    def __init__(self, title, author, pages, ISBN, price, audio_length):
        super().__init__(title, author, pages, ISBN, price)
        self.audio_length = audio_length

    def show_audiobook_details(self):
        return f"{super().get_book_details()}, Audio Length: {self.audio_length} hours"


#Let's create some books
    
book_1 = Book("The Republic", "Plato", 500, 656510, 1500)
book_2 = Book("The Art of War", "Sun Tzu", 620, 899820, 100)
book_3 = Book("The Rational Male", "Rollo Tomasi", 700, 778775, 2000)
book_4 = DigitalBook("Mellow", "Stanfield", 500, 786510, 1500, 2)
book_5 = AudioBook("Starship", "O'Rilley", 450, 222110, 2500, 2.5)

# Everytime you add (instantiate) a book here, modify the library as well. 

# Adding a Book subclass also requires modifying the Library class (particularly, the show_book method) to accommodate the changes.

# For instance, if we added another class of books like 'Historicals', we would override or extend its attributes from the book class, then create a method for accessing its details.DeprecationWarning

# We then take this method to the library class. 



#See this library 
library = Library()
library.add_books(book_1)
library.add_books(book_2)
library.add_books(book_3)
library.add_books(book_4)
library.add_books(book_5)

library.show_books()

