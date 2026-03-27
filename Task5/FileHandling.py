# File handling

users_list = [
    {"name": "Sushmanth", "age": 25, "role": "devops"},
    {"name": "Alice", "age": 30, "role": "frontend"},
    {"name": "Bob", "age": 35, "role": "backend"},
]

print("=== Task 7: File Handling ===")
filename = "team_data.txt"

# Write user details to file
with open(filename, "w") as file:
    for user in users_list:
        line = f"Name: {user['name']}, Age: {user['age']}, Role: {user['role']}\n"
        file.write(line)

# Read and display content
with open(filename, "r") as file:
    content = file.read()
    print("Content of team_data.txt:")
    print(content)

# Check if file is closed
print("Is file closed after with-block?", file.closed)
print("Program Completed")