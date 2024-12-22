import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Generate sample data
np.random.seed(42)
time = pd.date_range(start='2023-01-01', periods=12, freq='M')
sales = np.random.randint(100, 500, size=12)

categories = ['Setosa', 'Versicolor', 'Virginica']
average_petal_length = [1.5, 4.2, 5.6]

data_distribution = np.random.normal(loc=50, scale=15, size=500)

sepal_length = np.random.rand(100) * 7 + 1  # Range: 1 to 8
petal_length = np.random.rand(100) * 6 + 1  # Range: 1 to 7

# 1. Line chart for trends over time
plt.figure(figsize=(10, 6))
plt.plot(time, sales, marker='o', color='blue', label='Sales')
plt.title('Sales Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Sales ($)')
plt.grid(True)
plt.legend()
plt.show()

# 2. Bar chart for average petal length by species
plt.figure(figsize=(10, 6))
plt.bar(categories, average_petal_length, color=['red', 'green', 'blue'], edgecolor='black')
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.show()

# 3. Histogram of a numerical column
plt.figure(figsize=(10, 6))
plt.hist(data_distribution, bins=20, color='purple', edgecolor='black', alpha=0.7)
plt.title('Distribution of Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter plot of sepal length vs. petal length
plt.figure(figsize=(10, 6))
plt.scatter(sepal_length, petal_length, c='orange', alpha=0.6, edgecolor='black', label='Data Points')
plt.title('Sepal Length vs. Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.grid(True)
plt.show()