import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate data for a complex 3D surface
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
U, V = np.meshgrid(u, v)

# Parametric equations for a complex surface (twisted surface)
X = (1 + 0.5 * np.cos(U)) * np.cos(V)
Y = (1 + 0.5 * np.cos(U)) * np.sin(V)
Z = 0.5 * np.sin(U) * np.sin(2 * V)

# Create the 3D plot
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface with color shading
surface = ax.plot_surface(X, Y, Z, cmap='plasma', edgecolor='none', alpha=0.9)

# Customize the view angle
ax.view_init(elev=45, azim=60)

# Add color bar for reference
fig.colorbar(surface, shrink=0.5, aspect=10, label="Surface Height")

# Label the axes
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")

# Title
ax.set_title("Complex 3D Surface Plot")

# Display the plot
plt.show()