numbers = [12, 5, 18, 7, 24, 9, 30]

double_values = list(map(lambda x: x * 2, numbers))
greater_values = list(filter(lambda x: x > 10, numbers))
sorted_values = sorted(numbers, key=lambda x: x)

print("Original Numbers:", numbers)
print("Doubled Values:", double_values)
print("Numbers Greater Than 10:", greater_values)
print("Sorted Numbers:", sorted_values)
