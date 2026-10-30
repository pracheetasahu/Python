subjects = ["Python", "Java", "DBMS", "Machine Learning"]

print("Original List:", subjects)

subjects.append("Computer Networks")
print("After Adding:", subjects)

subjects.remove("Java")
print("After Removing:", subjects)

print("First Subject:", subjects[0])
print("Last Subject:", subjects[-1])

subjects[1] = "C Programming"
print("After Updating:", subjects)

print("Total Subjects:", len(subjects))

for subject in subjects:
    print(subject)
