from abc import ABC, abstractmethod
from functools import reduce

# ✅ Abstract Class
class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass


# ✅ Base Class
class User(AbstractUser):
    def __init__(self, name, id):
        self.name = name
        self.id = id


# ✅ Student Class
class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = int(fees)

    def get_details(self):
        return f"Student: {self.name}, ID: {self.id}, Dept: {self.dept}, Fees: {self.fees}"


# ✅ Faculty Class
class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = int(salary)

    def get_details(self):
        return f"Faculty: {self.name}, ID: {self.id}, Salary: {self.salary}"


# ✅ Temp Faculty
class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

    def get_details(self):
        return f"TempFaculty: {self.name}, ID: {self.id}, Salary: {self.salary}, Duration: {self.duration}"


# ✅ Data
students = [
    Student("Alice", 1, "CSE", 60000),
    Student("Bob", 2, "ECE", 40000),
    Student("Charlie", 3, "IT", 70000)
]

faculty = [
    Faculty("Dr.Smith", 101, 50000),
    Faculty("Dr.John", 102, 25000),
    TempFaculty("Dr.Ravi", 103, 35000, "6 months")
]


#  1. ALL DETAILS
print("\n ALL DETAILS")
list(map(lambda x: print(x.get_details()), students + faculty))


#  2. SORTING
students_sorted = sorted(students, key=lambda s: s.fees)
faculty_sorted = sorted(faculty, key=lambda f: f.salary)

print("\n SORTED STUDENTS")
list(map(lambda s: print(s.get_details()), students_sorted))

print("\n SORTED FACULTY")
list(map(lambda f: print(f.get_details()), faculty_sorted))


#  3. FILTERING
high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))

print("\n HIGH FEE STUDENTS")
list(map(lambda s: print(s.get_details()), high_fee_students))

print("\n HIGH SALARY FACULTY")
list(map(lambda f: print(f.get_details()), high_salary_faculty))


#  4. TOTAL (reduce)
total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)

print("\n TOTAL FEES:", total_fees)
print(" TOTAL SALARY:", total_salary)


#  5. COMBINED FUNCTIONAL (map + filter + reduce)
total_high_fees = reduce(
    lambda acc, s: acc + s,
    map(lambda s: s.fees, filter(lambda s: s.fees > 50000, students)),
    0
)

print("\n TOTAL HIGH FEES (Combined FP):", total_high_fees)