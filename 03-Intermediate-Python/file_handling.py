filename = "student.txt"

with open(filename, "w") as file:
    file.write("Student Name: Arun\n")
    file.write("Department: Computer Science\n")
    file.write("CGPA: 9.2\n")

print("Student information saved.")

with open(filename, "r") as file:
    content = file.read()

print("\nFile Contents:")
print(content)
