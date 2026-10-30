class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary")

    def display(self):
        print("Employee:", self.name)
        print("Salary:", self.__salary)

emp = Employee("Karthik", 45000)
emp.display()
emp.set_salary(52000)
print("Updated Salary:", emp.get_salary())
