#Medium Exercises

#Exercise 1

def sum_is_zero(lst):
    result = []
    n = len(lst)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if lst[i] + lst[j] + lst[k] == 0:
                    triplet = sorted([lst[i], lst[j], lst[k]])
                    if triplet not in result:
                        result.append(triplet)

    return result


#Exercise 2

def count_words(text):
    words = text.lower().replace('.', '').split(" ")
    output = dict()
    for word in words:
        if word in output:
            output[word] = output[word] + 1
        else:
            output[word] = 1

    return output


#Exercise 3

class Book:
    def __init__(self, title, author, year, is_checked_out = False):
        self.title = title
        self.author = author
        self.year = year
        self.is_checked_out = is_checked_out

    def checkout(self):
        self.is_checked_out = True

    def return_book(self):
        self.is_checked_out = False

    def __str__(self):
        return f"{self.title} by {self.author} (Checked out: {self.is_checked_out})"


class Library:
    def __init__(self, collection):
        self.collection = collection

    def add_book(self, book):
        self.collection.append(book)

    def list_books(self):
        for book in self.collection:
            status = "Checked out" if book.is_checked_out else "Available"
            print(f"{book.title} by {book.author} - {status}")

    def find_book(self, title):
        for book in self.collection:
            if title.lower() == book.title.lower():
                status = "Checked out" if book.is_checked_out else "Available"
                return f"{book.title} by {book.author} ({book.year}) - {status}"
        return f"{title} book was not found."

    def available_books(self):
        for book in self.collection:
            if not book.is_checked_out:
                print(f"{book.title} by {book.author} - Available")


b1 = Book("1984", "George Orwell", 1949)
b2 = Book("The Alchemist", "Paulo Coelho", 1988)

lib = Library([b1,b2])

lib.list_books()

b1.checkout()
lib.list_books()

found = lib.find_book("1984")
print(found)
