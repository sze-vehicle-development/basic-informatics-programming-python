import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
np.random.seed(42)  # For reproducibility
height = np.random.normal(170, 10, 100)  # Heights around 170 cm with a std dev of 10
weight = height * 0.5 + np.random.normal(50, 5, 100)  # Weight is roughly proportional to height

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(height, weight, color='teal', alpha=0.7, edgecolor='black', s=70, label="Height vs. Weight")

# Add title and labels
plt.title("Scatter Plot of Height vs. Weight")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.grid(True, linestyle='--', alpha=0.5)  # Add a light grid for readability

# Add legend
plt.legend()

# Display the plot
plt.show()