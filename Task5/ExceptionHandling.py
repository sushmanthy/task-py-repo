# Exception handling

def safe_divide():
    print("=== Task 6: Exception Handling Module ===")
    try:
        numerator = float(input("Enter numerator: "))
        denominator = float(input("Enter denominator: "))
        if denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = numerator / denominator
        print(f"Result: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except ZeroDivisionError as e:
        print(e)
    finally:
        print("Program Completed")

safe_divide()