def string_formatter(name, product):
    msg = f"{name} ordered {product} today!"
    width = 35
    
    print(f"Original: {msg}")
    print(f"Left padded:  '{msg:<{width}}'")
    print(f"Right padded: '{msg:>{width}}'")
    print(f"Center padded:'{msg:^{width}}'")

# Interactive
name = input("Enter name: ")
product = input("Enter product: ")
string_formatter(name, product)
