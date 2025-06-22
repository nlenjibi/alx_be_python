# book_class.py

class Book:
    """A class to represent a book using Python magic methods."""

    def __init__(self, title, author, year):
        """Constructor: Initializes a Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Called when an instance is about to be destroyed."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """User-friendly string representation of the object."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
