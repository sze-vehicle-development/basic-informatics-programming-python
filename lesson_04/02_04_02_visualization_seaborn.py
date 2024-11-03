import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate data for a complex function
x = np.linspace(-3, 3, 400)
y = np.linspace(-3, 3, 400)
X, Y = np.meshgrid(x, y)

# Define a complex function (e.g., multiple waves)
Z = np.sin(X**2 + Y**2) * np.cos(X - Y)

# Create a contour plot using Seaborn
plt.figure(figsize=(10, 8))
contour = sns.heatmap(Z, cmap='coolwarm', center=0, cbar_kws={'label': 'Intensity'}, xticklabels=False, yticklabels=False)

# Customize the plot
plt.title("Complex Contour Plot using Seaborn", fontsize=16)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# Display the plot
plt.show()