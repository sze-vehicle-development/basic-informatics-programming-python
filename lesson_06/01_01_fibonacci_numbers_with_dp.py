# Fibonacci with dynamic programming

def fibonacci(n):
    # Declare an array to store Fibonacci numbers.
    f = [0] * (n+1)
    # Base cases
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

# Test the function
n = 9
print(fibonacci(n))
n = 1
print(fibonacci(n))
# Large input
n = 100
print(fibonacci(n))
n = 1000
print(fibonacci(n))