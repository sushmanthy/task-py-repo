# Factorisl service using recursion

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("=== Task 4: Factorial Service ===")
try:
    print(f"Factorial of 5: {factorial(5)}")   # 120
    print(f"Factorial of 0: {factorial(0)}")   # 1
except ValueError as e:
    print(e)