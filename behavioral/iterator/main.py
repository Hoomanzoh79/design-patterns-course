class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# region iterable 
class BookShelf:
    """
    if we don't use iterator pattern, we have to expose the internal 
    structure of the bookshelf (the list of books) to the client code. 
    This can lead to tight coupling and makes it harder to change 
    the internal implementation of the bookshelf in the future. 
    for example,we would have to do this code : for book in bookshelf.books
    """
    def __init__(self):
        self.books:list[Book] = []

    def add_book(self, book):
        self.books.append(book)
    
    def __iter__(self):
        return BookShelfIterator(self)
#endregion

#region iterator
class BookShelfIterator:
    def __init__(self, bookshelf:BookShelf):
        self._bookshelf = bookshelf
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._bookshelf.books):
            book = self._bookshelf.books[self._index]
            self._index += 1
            return book
        else:
            raise StopIteration
# endregion

# region Generator
class BookShelfGenerator:
    """
    However,python gives us generators, which are a simpler way to create iterators.
    - if we do this,there is no need to create a separate iterator class, 
    and we can simply use a generator function to yield each book in the bookshelf.
    """
    def __init__(self):
        self.books:list[Book] = []

    def add_book(self, book):
        self.books.append(book)

    def __iter__(self):
        for book in self.books:
            yield book
# endregion

if __name__ == "__main__":
    bookshelf = BookShelfGenerator()
    bookshelf.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
    bookshelf.add_book(Book("To Kill a Mockingbird", "Harper Lee"))

    for book in bookshelf:
        print(f"{book.title} by {book.author}")
