# Base Class
class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id


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


# ✅ Sort Students by Fees
students.sort(key=lambda x: x.fees)

# ✅ Sort Faculty by Salary
faculty.sort(key=lambda x: x.salary)


# Display Results
print("Sorted Students (by fees):")
for s in students:
    print(s.name, s.fees)

print("\nSorted Faculty (by salary):")
for f in faculty:
    print(f.name, f.salary)