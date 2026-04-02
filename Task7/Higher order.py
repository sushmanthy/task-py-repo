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


# ✅ Higher Order Function
def process_users(users, func):
    return list(map(func, users))


# 👉 Using with map (Extract names)
names = process_users(students, lambda s: s.name)

print("Student Names:", names)

def process_users_filter(users, func):
    return list(filter(func, users))


# 👉 Get students with fees > 50000
high_fee_students = process_users_filter(students, lambda s: s.fees > 50000)

for s in high_fee_students:
    print(s.name, s.fees)