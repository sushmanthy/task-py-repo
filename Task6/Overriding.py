#Overriding
class User:
    def greet(self):
        print("Welcome User")


class Student(User):
    def greet(self):   # overriding
        print("Welcome Student")


class Faculty(User):
    def greet(self):   # overriding
        print("Welcome Faculty")


# Usage
s = Student()
f = Faculty()

s.greet()
f.greet()