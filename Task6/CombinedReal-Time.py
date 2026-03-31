class User:
    users_count = 0   # class variable
 
    def __init__(self, name, pwd):   # FIXED
        self.name = name
        self.pwd = pwd
        User.users_count += 1
 
    def get_name(self):
        return self.name
 
    def register(self):
        print(f"{self.name} registered")
        return self
 
    def login(self):
        print(f"{self.name} logged in")
        return self
 
    def greet(self):
        print("Welcome User")
        return self
 
 
class Student(User):
    def __init__(self, name, pwd):   # FIXED
        super().__init__(name, pwd)  # FIXED
 
    def greet(self):   # overriding
        print("Welcome Student")
        return self
 
 
class Faculty(User):
    def __init__(self, name, pwd):   # FIXED
        super().__init__(name, pwd)  # FIXED
 
    def greet(self):   # overriding
        print("Welcome Faculty")
        return self

s = Student("john", "123")
f = Faculty("admin", "999")

# Method chaining
s.login().greet().register()
print()

f.login().greet().register()
print()

# Bonus: total users
print("Total Users:", User.users_count)