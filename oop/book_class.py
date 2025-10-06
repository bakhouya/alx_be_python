class Book:
    # ================================================================================================
    # When we call the class, here we provide the title, author, and publication year of the book.
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    # ================================================================================================

    # ================================================================================================
    # When we delete the class, we call it to indicate that the book is being removed.
    def __del__(self):
        print(f"Deleting {self.title}")
    # ================================================================================================

    # ================================================================================================
    # This is how we represent the class in an informal way, returning a text string.
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    # ================================================================================================   

    # ================================================================================================
    # Here we represent the class in an official way, which is meant for developers and must be clear and unambiguous.
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
    # ================================================================================================