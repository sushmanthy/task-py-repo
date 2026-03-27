#user info manager
users_list = []  # Global list to store users

def create_user(name, age, role):
    user = {
        "name": name.title(),
        "age": age,
        "role": role
    }
    users_list.append(user)
    return user

# Add multiple users
create_user("sushmanth", 25, "devops")
create_user("alice", 30, "frontend")
create_user("bob", 35, "backend")

# Print all users
print("=== Task 1: User Info Manager ===")
for user in users_list:
    print(user)