import pandas as pd

# Load the CSV file
file_path = 'random_data.csv'  # Update this path if the file location differs
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(data.head())

# Display basic information about the dataset
print("\nDataset Information:")
print(data.info())

# Display summary statistics
print("\nSummary Statistics:")
print(data.describe())

# Check for any missing values
print("\nMissing Values in Each Column:")
print(data.isnull().sum())

# Group by 'City' and find average 'Score' in each city
print("\nAverage Score by City:")
print(data.groupby('City')['Score'].mean())

# Sort the dataset by 'Score' in descending order and show top 5 rows
print("\nTop 5 Records by Score:")
print(data.sort_values(by='Score', ascending=False).head())