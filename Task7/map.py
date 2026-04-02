# Sample Class
class Student:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees


# Sample Data
students = [
    Student("Alice", 60000),
    Student("Bob", 40000),
    Student("Charlie", 70000)
]


# ✅ Using map() to extract names
names = list(map(lambda s: s.name, students))

print("Student Names:", names)