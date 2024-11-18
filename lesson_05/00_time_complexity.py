# Plot different time complexities
import matplotlib.pyplot as plt
import numpy as np

# Define the input sizes
n = np.linspace(1, 100, 100)
# Define the time complexities
constant = np.ones(100)
logarithmic = np.log(n)
linear = n
log_linear = n * np.log(n)
quadratic = n**2
cubic = n**3
exponential = 2**n
# Plot the time complexities
plt.figure(figsize=(8, 12))
plt.plot(n, constant, label='O(1) - Constant', color='black')
plt.plot(n, logarithmic, label='O(log n) - Logarithmic', color='blue')
plt.plot(n, linear, label='O(n) - Linear', color='green')
plt.plot(n, log_linear, label='O(n log n) - Log-linear', color='orange')
plt.plot(n, quadratic, label='O(n^2) - Quadratic', color='red')
plt.plot(n, cubic, label='O(n^3) - Cubic', color='purple')
plt.plot(n, exponential, label='O(2^n) - Exponential', color='gray')
plt.xlabel('Input Size (n)')
plt.ylabel('Operations')
plt.xlim(1, 100)
plt.ylim(1, 100)
plt.title('Different Time Complexities')
plt.legend()
plt.grid(True)
plt.show()