employee = {
    "name": "Rahul",
    "age": 25,
    "department": "IT",
    "salary": 35000
}

print("Employee Details")
print("Name:", employee["name"])
print("Age:", employee["age"])
print("Department:", employee["department"])
print("Salary:", employee["salary"])

employee["salary"] = 40000
employee["city"] = "Chennai"

print("\nUpdated Details:", employee)

employee.pop("age")

print("After Removing Age:", employee)

print("\nAll Employee Information:")
for key, value in employee.items():
    print(key, ":", value)
