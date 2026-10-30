def factorial(number):
    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)


def fibonacci(position):
    if position <= 1:
        return position

    return fibonacci(position - 1) + fibonacci(position - 2)


value = 5

print("Factorial of", value, ":", factorial(value))

print("\nFibonacci Series:")
for i in range(7):
    print(fibonacci(i), end=" ")
print()
