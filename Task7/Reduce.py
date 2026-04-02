from functools import reduce

# Sample Classes
class Student:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees

class Faculty:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


# Sample Data
students = [
    Student("Alice", 60000),
    Student("Bob", 40000),
    Student("Charlie", 70000)
]

faculty = [
    Faculty("Dr.Smith", 50000),
    Faculty("Dr.John", 25000),
    Faculty("Dr.Ravi", 35000)
]


# ✅ Total Fees
total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)

# ✅ Total Salary
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)


print("Total Fees:", total_fees)
print("Total Salary:", total_salary)