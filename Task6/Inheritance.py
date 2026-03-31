#Inheritance

# Parent class
class User:
    def register(self):
        print("User Registered")

    def login(self):
        print("User Logged In")


# Child class 1
class Student(User):
    def student_greet(self):
        print("Hello Student")


# Child class 2
class Faculty(User):
    def faculty_greet(self):
        print("Hello Faculty")


# Multilevel inheritance
class TempFaculty(Faculty):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")


# Usage
s = Student()
s.register()        # parent method
s.login()
s.student_greet()

f = Faculty()
f.register()
f.faculty_greet()

t = TempFaculty()
t.login()
t.faculty_greet()
t.tempFaculty_greet()