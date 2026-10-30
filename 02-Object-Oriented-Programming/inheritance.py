class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_teacher(self):
        self.display_person()
        print("Subject:", self.subject)


teacher = Teacher("Ravi", 35, "Mathematics")
teacher.display_teacher()
