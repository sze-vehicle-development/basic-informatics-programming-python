# Recursive Fibonacci sequence
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test the function
n = 3
print(fibonacci(n))
n = 5
print(fibonacci(n))
n = 8
print(fibonacci(n))
n = 10
print(fibonacci(n))
n = 25
print(fibonacci(n))