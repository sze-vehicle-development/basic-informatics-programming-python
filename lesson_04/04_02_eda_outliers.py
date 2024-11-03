import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Generate random data with some outliers
num_records = 150
data = {
    'Age': np.random.normal(35, 10, num_records).astype(int),  # Ages centered around 35 with a standard deviation of 10
    'Income': np.random.normal(50000, 15000, num_records).round(2)  # Incomes centered around $50,000 with outliers
}

# Introduce outliers in 'Income'
outliers_income = [150000, 200000, 220000, 300000]  # Outlier incomes
data['Income'][:len(outliers_income)] = outliers_income  # Insert these outliers at the start

# Create DataFrame
df_outliers = pd.DataFrame(data)

# Plot Histogram for Age with Outliers
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(df_outliers['Age'], bins=15, color='skyblue', edgecolor='black')
plt.title('Age Distribution with Outliers')
plt.xlabel('Age')
plt.ylabel('Frequency')

# Plot Histogram for Income with Outliers
plt.subplot(1, 2, 2)
plt.hist(df_outliers['Income'], bins=15, color='salmon', edgecolor='black')
plt.title('Income Distribution with Outliers')
plt.xlabel('Income ($)')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# Plot Boxplots for Age and Income with Outliers
plt.figure(figsize=(10, 6))

# Boxplot for Age
plt.subplot(1, 2, 1)
plt.boxplot(df_outliers['Age'], patch_artist=True, boxprops=dict(facecolor="skyblue"))
plt.title('Boxplot of Age')
plt.ylabel('Age')

# Boxplot for Income
plt.subplot(1, 2, 2)
plt.boxplot(df_outliers['Income'], patch_artist=True, boxprops=dict(facecolor="salmon"))
plt.title('Boxplot of Income with Outliers')
plt.ylabel('Income ($)')

plt.tight_layout()
plt.show()

plt.scatter(df_outliers['Age'], df_outliers['Income'], color='teal', alpha=0.7, edgecolor='black', s=70, label="Age vs. Income")
plt.title("Scatter Plot of Age vs. Income with Outliers")
plt.xlabel("Age")
plt.ylabel("Income ($)")
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.show()