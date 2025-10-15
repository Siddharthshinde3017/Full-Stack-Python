class person:
    def display (self):
        print("I am Person")

class Student(person):
    def role(self):
        print("I am student")

class Tescher(person):
    def role(self):
        print("I am Teacher")

class TeacherAssistant(Student,Tescher):
    def assist(self):
        print("I am Teacher Assistant")

ta = TeacherAssistant()
ta.assist()
ta.role()
ta.role()
ta.display()