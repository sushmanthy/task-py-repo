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


# ✅ Filter Students with fees > 50000
high_fee_students = list(filter(lambda s: s.fees > 50000, students))

# ✅ Filter Faculty with salary > 30000
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))


# Display Results
print("High Fee Students:")
for s in high_fee_students:
    print(s.name, s.fees)

print("\nHigh Salary Faculty:")
for f in high_salary_faculty:
    print(f.name, f.salary)