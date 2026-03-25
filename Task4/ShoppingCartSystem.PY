#Shopping Cart System

cart = []  # List of {'name': str, 'price': float, 'qty': int}

def add_item(name, price, qty):
    cart.append({'name': name, 'price': price, 'qty': qty})
    print(f"Added {qty} x {name} (${price} each)")

def remove_item(name):
    original_count = len(cart)
    cart[:] = [item for item in cart if item['name'].lower() != name.lower()]
    if len(cart) < original_count:
        print(f"Removed {name}")
    else:
        print("Item not found")

def calculate_total():
    return sum(item['price'] * item['qty'] for item in cart)

def display_cart():
    if not cart:
        print("Your cart is empty.")
        return
    total = calculate_total()
    print(f"\n{'='*45}")
    print(f"{'PRODUCT':<20} {'QTY':<5} {'UNIT PRICE':<12} {'LINE TOTAL'}")
    print(f"{'='*45}")
    for item in cart:
        line_total = item['price'] * item['qty']
        print(f"{item['name']:<20} {item['qty']:<5} ${item['price']:>9.2f} ${line_total:>9.2f}")
    print(f"{'='*45}")
    print(f"{'GRAND TOTAL:':<38} ${total:>7.2f}")
    print(f"{'='*45}")

# Interactive menu loop
while True:
    print("\n1. Add item  2. Remove item  3. Display cart  4. Total  5. Quit")
    choice = input("Choose: ")
    if choice == '1':
        add_item(input("Product: "), float(input("Price: ")), int(input("Qty: ")))
    elif choice == '2':
        remove_item(input("Product name: "))
    elif choice == '3':
        display_cart()
    elif choice == '4':
        print(f"Total bill: ${calculate_total():.2f}")
    elif choice == '5':
        break