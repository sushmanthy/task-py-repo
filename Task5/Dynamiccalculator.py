#Dynamic calculator

def calculate_total(*numbers):
    total = sum(numbers)
    if len(numbers) == 0:
        average = 0
    else:
        average = total / len(numbers)
    return total, average

print("=== Task 2: Dynamic Calculator ===")
total, avg = calculate_total(10, 20, 30, 40)
print(f"Total: {total}, Average: {avg:.2f}")