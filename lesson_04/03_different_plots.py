import matplotlib.pyplot as plt

# Sample data for line plot
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [300, 400, 350, 450, 500, 600]

# Create line plot
plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker='o', color='blue', linestyle='-', linewidth=2)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.grid(True)
plt.show()

# Scatter plot
import numpy as np

# Sample data for scatter plot
np.random.seed(0)
height = np.random.normal(170, 10, 50)  # Heights around 170 cm
weight = height * 0.5 + np.random.normal(20, 5, 50)  # Weight roughly proportional to height

# Create scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(height, weight, color='purple', edgecolor='black', alpha=0.7)
plt.title("Height vs Weight")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.grid(True)
plt.show()

# Pie chart
# Sample data for pie chart
categories = ['Product A', 'Product B', 'Product C', 'Product D']
market_share = [30, 25, 20, 25]

# Create pie chart
plt.figure(figsize=(6, 6))
plt.pie(market_share, labels=categories, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'salmon', 'lightgreen', 'orange'])
plt.title("Market Share by Product")
plt.show()
