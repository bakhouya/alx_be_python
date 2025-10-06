# ================================================================================================
# Here I create a base class called Book , this class accepts title and author and return a string 

class Book:
    def __init__(self, title, author):
        self.title = title   
        self.author = author 

    def __str__(self):
        return f"Book: {self.title} by {self.author}"
# ================================================================================================

# ================================================================================================
# Here I create a derived class called EBook, this class call a Book class and add accepts file_size
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author) 
        self.file_size = file_size      

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"
# ================================================================================================


# ================================================================================================
# Here I create a derived class called PrintBook, this class call a Book class and add accepts page_count
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  
        self.page_count = page_count    

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"
# ================================================================================================

# ================================================================================================
# Here I create class Library, this class give def to create new book and return sreing 
class Library:
    def __init__(self):
        self.books = []  

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)
# ================================================================================================