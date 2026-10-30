class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return self.title + " - " + str(self.pages) + " pages"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.pages == other.pages

book1 = Book("Python Basics", 250)
book2 = Book("Java Guide", 300)
book3 = Book("Python Advanced", 250)

print(book1)
print("Page Count:", len(book1))
print("Same Page Count:", book1 == book3)
print("Different Page Count:", book1 == book2)
