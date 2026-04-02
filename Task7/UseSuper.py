# Base Class
class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

# Child Class: Student
class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)   # reuse parent constructor
        self.dept = dept
        self.fees = fees


# Child Class: Faculty
class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary


# Multi-level Inheritance: TempFaculty
class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration


# Testing
s = Student("Alice", 1, "CSE", 60000)
f = Faculty("Dr.Smith", 101, 50000)
tf = TempFaculty("Dr.Ravi", 103, 35000, "6 months")

print(s.name, s.id, s.dept, s.fees)
print(f.name, f.id, f.salary)
print(tf.name, tf.id, tf.salary, tf.duration)