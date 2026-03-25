#Unique Vistor Counter

visitors = set()  # Automatically avoids duplicates

def add_visitor(name):
    visitors.add(name)  # Set ignores if already present
    print(f"✅ Added: {name}")

def print_unique_count():
    print(f"Total unique visitors: {len(visitors)}")
    print(f"All visitors: {sorted(visitors)}")

add_visitor("Alice")
add_visitor("Bob")
add_visitor("Alice")  # Ignored (duplicate)
add_visitor("Carol")

print_unique_count()