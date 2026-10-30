print("Numbers from 1 to 10")

for number in range(1, 11):
    print(number, end=" ")

print("\n\nMultiplication Table")

number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)

print("\nCountdown using While Loop")

count = 5

while count >= 1:
    print(count)
    count -= 1

print("Blast Off!")
