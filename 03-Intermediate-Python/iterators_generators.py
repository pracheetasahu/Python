class NumberIterator:
    def __init__(self, limit):
        self.current = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            value = self.current
            self.current += 1
            return value
        raise StopIteration


def even_numbers(limit):
    for number in range(2, limit + 1, 2):
        yield number


numbers = NumberIterator(5)

print("Using Iterator:")
for value in numbers:
    print(value, end=" ")

print("\nUsing Generator:")
for value in even_numbers(10):
    print(value, end=" ")
print()
