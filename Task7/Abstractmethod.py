from abc import ABC, abstractmethod
from functools import reduce

# ✅ Task 2: Abstract Base Class
class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass


# Base Class
class User(AbstractUser):
    def __init__(self, name, id):
        self.name = name
        self.id = id

# Child Class: Student
class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)   # reuse parent constructor
        self.dept = dept
        self.fees = fees
    def get_details(self):
        return f"student: {self.name}, ID: {self.id}, Dept: {self.dept}, Fees: {self.fees}"    

# Child Class: Faculty
class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary
    def get_details(self):        
        return f"Faculty: {self.name}, ID: {self.id}, Salary: {self.salary}"   


# Multi-level Inheritance: TempFaculty
class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration
    def get_details(self):
        return f"TempFaculty: {self.name}, ID: {self.id}, Salary: {self.salary}, Duration: {self.duration}"

# Testing
s = Student("Alice", 1, "CSE", 60000)
f = Faculty("Dr.Smith", 101, 50000)
tf = TempFaculty("Dr.Ravi", 103, 35000, "6 months")

print(s.get_details())
print(f.get_details())
print(tf.get_details())