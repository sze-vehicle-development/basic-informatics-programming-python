def first_function():
    print('Hello, World!')

def add_and_multiply_with_const(c, x, y):
    return c * (x + y)

x = 10
y = 8
z = add_and_multiply_with_const(2, x, y)
print(z)
z2 = add_and_multiply_with_const(6, x, y)
print(z2)