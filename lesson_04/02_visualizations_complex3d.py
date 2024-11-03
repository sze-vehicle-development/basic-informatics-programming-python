import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate data for the 3D surface plot
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))  # Using a radial sine function for surface

# Generate random points for scatter plot on the surface
num_points = 100
x_points = np.random.uniform(-5, 5, num_points)
y_points = np.random.uniform(-5, 5, num_points)
z_points = np.sin(np.sqrt(x_points**2 + y_points**2)) + np.random.normal(0, 0.1, num_points)  # Add some noise

# Create the 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the 3D surface
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.7)
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, label="Surface Height")

# Overlay a 3D scatter plot on the surface
ax.scatter(x_points, y_points, z_points, color='red', s=50, label="Random Points")

# Label the axes
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")

# Title and legend
ax.set_title("3D Surface Plot with Overlayed 3D Scatter Points")
ax.legend(loc="upper left")

# Show the plot
plt.show()