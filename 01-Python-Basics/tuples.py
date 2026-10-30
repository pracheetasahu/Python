student = ("Arun", 20, "CSE", 9.2)

print("Student Details:", student)
print("Name:", student[0])
print("Age:", student[1])
print("Department:", student[2])
print("CGPA:", student[3])

print("Total Details:", len(student))

if "CSE" in student:
    print("Department found in tuple")

for item in student:
    print(item)
