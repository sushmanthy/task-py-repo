#Employee Management system

employees =[]
def add_employee():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    role = input("Enter role: ")
    salary = float(input("Enter salary: "))
    emp = {'name': name, 'age': age, 'role': role, 'salary': salary}
    employees.append(emp)
    print(f"Added {name}")

def display_employees():
    if not employees:
        print("No employees found.")
        return
    for emp in employees:
        print(f"Name: {emp['name']}, Age: {emp['age']}, Role: {emp['role']}, Salary: ${emp['salary']}")

def update_employee():
    name = input("Enter name to update: ")
    for emp in employees:
        if emp['name'] == name:
            field = input("Enter field (age/role/salary): ")
            if field in ['age', 'role', 'salary']:
                value = int(input("Enter new value: ")) if field == 'age' else \
                        input("Enter new value: ") if field == 'role' else \
                        float(input("Enter new value: "))
                emp[field] = value
                print(f"Updated {name}'s {field}")
                return
    print("Employee not found.")

def delete_employee():
    name = input("Enter name to delete: ")
    for i, emp in enumerate(employees):
        if emp['name'] == name:
            del employees[i]
            print(f"Deleted {name}")
            return
    print("Employee not found.")

while True:
    print("\n1. Add  2. Display  3. Update  4. Delete  5. Quit")
    choice = input("Choose: ")
    if choice == '1': add_employee()
    elif choice == '2': display_employees()
    elif choice == '3': update_employee()
    elif choice == '4': delete_employee()
    elif choice == '5': break
    else: print("Invalid choice.")