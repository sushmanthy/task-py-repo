#Course enrollement system

enrollments = []  # List of {'name': str, 'courses': list}

def add_student(name, courses):
    enrollments.append({'name': name, 'courses': courses})
    print(f"Enrolled {name} in {len(courses)} courses: {', '.join(courses)}")

def update_courses(name, new_courses):
    for student in enrollments:
        if student['name'].lower() == name.lower():
            student['courses'] = new_courses
            print(f"Updated {name}: {', '.join(new_courses)}")
            return True
    print("Student not found")
    return False

def display_student(name):
    for student in enrollments:
        if student['name'].lower() == name.lower():
            print(f"\n{'='*30}")
            print(f"Student: {student['name']}")
            print(f"Courses ({len(student['courses'])}):")
            for i, course in enumerate(student['courses'], 1):
                print(f"  {i}. {course}")
            print(f"{'='*30}")
            return
    print("Student not found")

def display_all():
    if not enrollments:
        print("No enrollments")
        return
    print(f"\n{'='*50}")
    print(f"All Enrollments ({len(enrollments)} students)")
    print(f"{'='*50}")
    for student in enrollments:
        print(f"{student['name']:<15}: {', '.join(student['courses'])}")
    print(f"{'='*50}")

# Interactive menu
while True:
    print("\n1.Add student  2.Update courses  3.Display student  4.All students  5.Quit")
    choice = input("Choose: ")
    if choice == '1':
        name = input("Student name: ")
        courses = input("Courses (comma-separated): ").split(',')
        courses = [c.strip() for c in courses]
        add_student(name, courses)
    elif choice == '2':
        name = input("Student name: ")
        courses = input("New courses (comma-separated): ").split(',')
        courses = [c.strip() for c in courses]
        update_courses(name, courses)
    elif choice == '3':
        display_student(input("Student name: "))
    elif choice == '4':
        display_all()
    elif choice == '5':
        break