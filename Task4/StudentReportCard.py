# Student Report Card System

def calculate_total_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

def get_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    else:
        return 'C'

def print_report(student_name, marks_list):
    total, avg = calculate_total_average(marks_list)
    grade = get_grade(avg)
    subjects = ['Math', 'Science', 'English']
    print(f"\n{'='*40}")
    print(f"    REPORT CARD: {student_name.upper()}")
    print(f"{'='*40}")
    for subject, mark in zip(subjects, marks_list):
        print(f"{subject:12}: {mark:>4}")
    print(f"{'='*40}")
    print(f"Total Marks: {total:>24}")
    print(f"Average:     {avg:>22.1f}")
    print(f"Grade:       {grade:>25}")
    print(f"{'='*40}")

students = {}
while True:
    name = input("Student name (or 'done'): ")
    if name == 'done':
        break
    marks = list(map(int, input("Marks (Math Science English): ").split()))
    students[name] = marks

for name, marks in students.items():
    print_report(name, marks)