# Memory optimization techniques

def square_generator(n):
    for i in range(1, n + 1):
        yield i * i

print("=== Task 5: Memory Optimization (Generator) ===")
n = 5
normal_list = [i * i for i in range(1, n + 1)]
gen = square_generator(n)

print("Normal list:", normal_list)
print("Generator:", gen)
print("Type of list:", type(normal_list))
print("Type of generator:", type(gen))

print("Yielded values from generator:")
for val in gen:
    print(val) 