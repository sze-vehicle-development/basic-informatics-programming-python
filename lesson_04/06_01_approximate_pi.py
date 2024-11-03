import numpy as np
import matplotlib.pyplot as plt

# Number of random points
num_points = 10000

# Generate random (x, y) points in the range [-1, 1] x [-1, 1]
x = np.random.uniform(-1, 1, num_points)
y = np.random.uniform(-1, 1, num_points)

# Calculate the distance of each point from the origin
distance = np.sqrt(x**2 + y**2)

# Count points that fall inside the unit circle (distance <= 1)
inside_circle = distance <= 1
num_inside_circle = np.sum(inside_circle)

# Approximate pi using the ratio of points inside the circle
pi_approx = 4 * num_inside_circle / num_points
print(f"Approximated value of π: {pi_approx}")

# Plot the points
plt.figure(figsize=(8, 8))
plt.scatter(x[inside_circle], y[inside_circle], color='blue', s=1, label="Inside Circle")
plt.scatter(x[~inside_circle], y[~inside_circle], color='red', s=1, label="Outside Circle")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Monte Carlo Simulation to Approximate π")
plt.legend()
plt.axis("equal")
plt.show()