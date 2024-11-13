# Step 1: Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Load the dataset
# Assuming you have a CSV file named 'data.csv'
df = pd.read_csv('data.csv')

# Step 3: Explore the dataset
print("First 5 rows of the dataset:")
print(df.head())

print("\nSummary statistics:")
print(df.describe())

print("\nData types and missing values:")
print(df.info())

# Step 4: Basic Data Analysis
# Example: Calculate mean of a numeric column
mean_value = df['numeric_column'].mean()
print(f"\nMean of numeric_column: {mean_value}")

# Step 5: Visualizations
# Example: Histogram
plt.figure(figsize=(10, 6))
df['numeric_column'].hist(bins=30)
plt.title('Histogram of Numeric Column')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Example: Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['numeric_column1'], df['numeric_column2'])
plt.title('Scatter Plot of Numeric Column1 vs Numeric Column2')
plt.xlabel('Numeric Column1')
plt.ylabel('Numeric Column2')
plt.show()

# Step 6: Findings and Observations
# Add your observations here
