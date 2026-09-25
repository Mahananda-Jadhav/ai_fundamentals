class Book:
    def __init__(self, title, author, pages):
        # Store title, author, and pages on this object
        self.title = title
        self.author = author
        self.pages = pages

    def summary(self):
        # Return a one-line string matching the expected output format
        return f"{self.title} by {self.author}, {self.pages} pages."

# Creating the three separate Book objects
book1 = Book("Deep Work", "Cal Newport", 304)
book2 = Book("Sapiens", "Yuval Noah Harari", 443)
book3 = Book("Atomic Habits", "James Clear", 320)

# Collecting the three objects into a list
book_list = [book1, book2, book3]

# Loop through the list, call summary() on each book, and print the result
for book in book_list:
    print(book.summary())
