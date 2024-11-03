import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
months = np.arange(1, 13)  # Months from 1 to 12
sales = np.array([230, 340, 300, 400, 370, 450, 480, 500, 520, 480, 460, 530])  # Monthly sales data

# Create the line plot
plt.figure(figsize=(10, 6))
plt.plot(months, sales, color='blue', marker='o', linestyle='-', linewidth=2, markersize=6, label='Sales')

# Add title and labels
plt.title("Monthly Sales Data")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.xticks(months)  # Set x-ticks to each month
plt.grid(True)  # Add grid for better readability

# Show legend
plt.legend()

# Display the plot
plt.show()