def add(x, y):
    return x + y  # Pure function: No side effects or reliance on external state

# First-class and higher order functions
def apply_twice(func, value):
    return func(func(value))
print(apply_twice(lambda x: x + 1, 5))

# Function composition
def increment(x):
    return x + 1
def double(x):
    return x * 2

# Function composition in a pipeline
result = double(increment(5))
print(result)