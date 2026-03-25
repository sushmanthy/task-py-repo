# Login and User Validation System
# Store users: {username: password}
users = {
    'alice': 'pass123',
    'bob': 'secret456',
    'admin': 'admin789'
}

def validate_login(username, password):
    if username in users and users[username] == password:
        print("✅ Login successful! Welcome back.")
        return True
    else:
        print("❌ Login failed! Invalid credentials.")
        return False

# Interactive login (3 attempts)
attempts = 3
while attempts > 0:
    username = input("Username: ").lower()
    password = input("Password: ")
    if validate_login(username, password):
        print("Access granted!")
        break
    attempts -= 1
    print(f"{attempts} attempts left.")

if attempts == 0:
    print("Account locked. Try again later.") 