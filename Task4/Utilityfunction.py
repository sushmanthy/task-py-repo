#utility function to display number in various formats

def number_utils(num):
    print(f"\n{'='*40}")
    print(f"Input Number: {num}")
    print(f"Binary:   {bin(num)[2:].upper():>15}")
    print(f"Octal:    {oct(num)[2:].upper():>15}")
    print(f"Hex:      {hex(num)[2:].upper():>15}")
    print(f"Commas:   {num:,}")
    print(f"Scientific:{num:>10.2e}")
    print(f"{'='*40}")

# Interactive
while True:
    try:
        n = int(input("Enter number (0 to quit): "))
        if n == 0:
            break
        number_utils(n)
    except ValueError:
        print("Enter valid integer!")