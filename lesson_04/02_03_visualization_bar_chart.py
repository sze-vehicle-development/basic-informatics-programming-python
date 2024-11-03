import matplotlib.pyplot as plt
import numpy as np

# Data for the bar chart
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = [300, 400, 320, 450, 500, 490, 550, 600, 580, 620, 610, 700]

# Create the bar chart
plt.figure(figsize=(12, 6))
plt.bar(months, sales, color="skyblue", edgecolor="black", linewidth=1.2)

# Add title and labels
plt.title("Monthly Sales Data", fontsize=16)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales ($)", fontsize=12)
plt.xticks(rotation=45)  # Rotate month labels for better readability
plt.grid(axis='y', linestyle='--', alpha=0.6)  # Add horizontal grid lines for clarity

# Show values on top of each bar
for i, value in enumerate(sales):
    plt.text(i, value + 20, f"${value}", ha="center", va="bottom")

# Display the plot
plt.show()