def create_account(accounts, name, balance):
    """Create a new account with the given name and initial balance."""
    if name in accounts:
        print(f"Account with name '{name}' already exists.")
        return False
    accounts[name] = balance
    print(f"Account created for {name} with balance: {balance}")
    return True

def deposit(accounts, name, amount):
    """Deposit money into the given account."""
    if name not in accounts:
        print(f"Account '{name}' does not exist.")
        return False
    if amount <= 0:
        print("Deposit amount must be greater than zero.")
        return False
    accounts[name] += amount
    print(f"Deposited {amount} into {name}'s account. New balance: {accounts[name]}")
    return True

def withdraw(accounts, name, amount):
    """Withdraw money from the given account."""
    if name not in accounts:
        print(f"Account '{name}' does not exist.")
        return False
    if amount <= 0:
        print("Withdrawal amount must be greater than zero.")
        return False
    if accounts[name] < amount:
        print("Insufficient balance.")
        return False
    accounts[name] -= amount
    print(f"Withdrew {amount} from {name}'s account. New balance: {accounts[name]}")
    return True

def check_balance(accounts, name):
    """Check the balance of the given account."""
    if name not in accounts:
        print(f"Account '{name}' does not exist.")
        return None
    print(f"Balance of {name}'s account: {accounts[name]}")
    return accounts[name]
if __name__ == "__main__":
    accounts = {}  # dictionary to store account_name -> balance

    create_account(accounts, "Alice", 1000)
    deposit(accounts, "Alice", 500)
    withdraw(accounts, "Alice", 200)
    check_balance(accounts, "Alice")

    print("\nAll accounts:", accounts)
