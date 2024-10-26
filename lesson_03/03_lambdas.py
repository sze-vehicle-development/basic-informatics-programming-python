squares = list(map(lambda x: x**2, range(10)))
add = lambda a, b: a + b
print(add(2, 3))
print(squares)
# Items unsorted
square = lambda x: x ** 2
print(square(5))
items = [("product1", 10), ("product2", 9), ("product3", 12)]
sorted_items = sorted(items, key=lambda x: x[1])
print(sorted_items)
# Use as a function argument
def apply_func(x, fn):
    return fn(x)
print(apply_func(3, lambda x: x**2))