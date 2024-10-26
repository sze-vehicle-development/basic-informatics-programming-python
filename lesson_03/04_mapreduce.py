# Map
x = map(lambda x: x**2, [1, 2, 3])
print(list(x))
# Reduce
from functools import reduce
x = reduce(lambda x, y: x + y, [1, 2, 3, 4])
print(x)
# Filter
x = filter(lambda x: x % 2 == 0, [1, 2, 3, 4])
print(list(x))