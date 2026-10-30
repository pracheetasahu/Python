def divide_numbers():
    try:
        first = int(input("Enter first number: "))
        second = int(input("Enter second number: "))
        answer = first / second
        print("Division Result:", answer)
    except ValueError:
        print("Please enter valid numbers.")
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
    finally:
        print("Calculation finished.")

divide_numbers()
