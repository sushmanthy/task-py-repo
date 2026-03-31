# Encapsulation
class User:
    def _init_(self):
        self.user_name = None   # private variable
        self.pwd = None         # private variable

    def set_user(self, user_name, pwd):
        self.user_name = user_name
        self.pwd = pwd

    def get_user(self):
        return self.user_name   # password hidden

    def register(self):
        print(f"Registering user: {self.user_name}")

    def login(self):
        print(f"Logging in: {self.user_name}")


# Usage
u = User()
u.set_user("john", "1234")
u.register()
u.login()