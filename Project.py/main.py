import mysql.connector
from abc import ABC, abstractmethod
from functools import reduce
from datetime import datetime

# ---------------- DATABASE CONNECTION ----------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="expense_db"
)

cursor = conn.cursor()

# ---------------- ABSTRACT CLASS ----------------
class BaseSystem(ABC):

    @abstractmethod
    def get_details(self):
        pass


# ---------------- USER CLASS ----------------
class User(BaseSystem):
    def _init_(self, name):
        self.__name = name   # encapsulation

    def create_user(self):
        query = "INSERT INTO users (name) VALUES (%s)"
        cursor.execute(query, (self.__name,))
        conn.commit()
        print("✅ User added successfully!")

    def get_details(self):
        print(f"User: {self.__name}")


# ---------------- EXPENSE CLASS ----------------
class Expense(User):   # inheritance

    def _init_(self, name):
        super()._init_(name)

    # ADD EXPENSE
    def add_expense(self, user_id, amount, category, description, date):
        query = """INSERT INTO expenses (user_id, amount, category, description, date)
                   VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(query, (user_id, amount, category, description, date))
        conn.commit()
        print("💸 Expense added!")

    # VIEW EXPENSES (JOIN)
    def view_expenses(self, user_id):
        query = """
        SELECT u.name, e.amount, e.category, e.description, e.date
        FROM users u
        JOIN expenses e ON u.user_id = e.user_id
        WHERE u.user_id = %s
        """
        cursor.execute(query, (user_id,))
        data = cursor.fetchall()

        print("\n📊 Expenses:")
        for row in data:
            print(row)

        return data

    # FILTER EXPENSES
    def filter_expenses(self, expenses, category=None, date=None):
        result = expenses

        if category:
            result = list(filter(lambda x: x[2] == category, result))

        if date:
            result = [x for x in result if str(x[4]) == date]

        return result

    # TOTAL EXPENSE (map + reduce)
    def total_expense(self, expenses):
        amounts = list(map(lambda x: x[1], expenses))
        total = reduce(lambda a, b: a + b, amounts, 0)
        return total

    # CATEGORY-WISE SPENDING
    def category_wise(self, expenses):
        categories = {x[2] for x in expenses}

        result = {
            cat: sum([x[1] for x in expenses if x[2] == cat])
            for cat in categories
        }

        return result

    # DELETE EXPENSE
    def delete_expense(self, exp_id):
        cursor.execute("DELETE FROM expenses WHERE exp_id = %s", (exp_id,))
        conn.commit()
        print("🗑️ Deleted successfully")

    # UPDATE EXPENSE
    def update_expense(self, exp_id, amount):
        cursor.execute("UPDATE expenses SET amount=%s WHERE exp_id=%s", (amount, exp_id))
        conn.commit()
        print("✏️ Updated successfully")

    # MONTHLY REPORT
    def monthly_report(self, expenses):
        report = {}

        for e in expenses:
            month = str(e[4])[:7]   # YYYY-MM
            report[month] = report.get(month, 0) + e[1]

        return report

    # HIGHEST EXPENSE (reduce)
    def highest_expense(self, expenses):
        return reduce(lambda a, b: a if a[1] > b[1] else b, expenses)

    # SMART INSIGHT
    def smart_insight(self, expenses):
        cat_data = self.category_wise(expenses)

        highest_cat = max(cat_data, key=cat_data.get)

        print(f"\n⚠️ Insight: You are spending too much on {highest_cat}!")


# ---------------- MAIN PROGRAM ----------------

exp = Expense()

# Create user (run once)
# exp.create_user()

user_id = 1

# Add expenses
exp.add_expense(user_id, 500, "Food", "Lunch", "2026-04-01")
exp.add_expense(user_id, 1500, "Shopping", "Clothes", "2026-04-02")
exp.add_expense(user_id, 800, "Travel", "Bus", "2026-04-03")
exp.add_expense(user_id, 1200, "Food", "Dinner", "2026-04-04")

# View
data = exp.view_expenses(user_id)

# Filter
print("\n🔍 Filtered (Food):")
print(exp.filter_expenses(data, category="Food"))

# Total
print("\n💰 Total Expense:", exp.total_expense(data))

# Category-wise
print("\n📂 Category-wise:")
print(exp.category_wise(data))

# Monthly report
print("\n📅 Monthly Report:")
print(exp.monthly_report(data))

# Highest expense
print("\n🔥 Highest Expense:")
print(exp.highest_expense(data))

# Smart insight
exp.smart_insight(data)