class Library:
    library_name = "Central Library"
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Library.total_books += 1

    def display(self):
        print("Library:", Library.library_name)
        print("Book:", self.title)
        print("Author:", self.author)

book1 = Library("Python Basics", "James")
book2 = Library("Data Science", "Robert")

book1.display()
print()
book2.display()
print("Total Books:", Library.total_books)
