class Academic:
    def show_marks(self):
        print("Academic Marks: 85")

class Sports:
    def show_sports_score(self):
        print("Sports Score: 90")

class Student(Academic, Sports):
    def display(self):
        print("Student Performance")
        self.show_marks()
        self.show_sports_score()

student = Student()
student.display()
