import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate random data for a new dataset
np.random.seed(0)  # For reproducibility
num_records = 200

data = {
    'Age': np.random.randint(18, 70, size=num_records),  # Random ages between 18 and 70
    'Income': np.random.normal(50000, 15000, size=num_records).round(2),  # Normal distribution around $50,000
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot Histogram for Age
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(df['Age'], bins=15, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')

# Plot Histogram for Income
plt.subplot(1, 2, 2)
plt.hist(df['Income'], bins=15, color='salmon', edgecolor='black')
plt.title('Income Distribution')
plt.xlabel('Income ($)')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# Plot Boxplots for Age and Income
plt.figure(figsize=(10, 6))

# Boxplot for Age
plt.subplot(1, 2, 1)
plt.boxplot(df['Age'], patch_artist=True, boxprops=dict(facecolor="skyblue"))
plt.title('Boxplot of Age')
plt.ylabel('Age')

# Boxplot for Income
plt.subplot(1, 2, 2)
plt.boxplot(df['Income'], patch_artist=True, boxprops=dict(facecolor="salmon"))
plt.title('Boxplot of Income')
plt.ylabel('Income ($)')

plt.tight_layout()
plt.show()