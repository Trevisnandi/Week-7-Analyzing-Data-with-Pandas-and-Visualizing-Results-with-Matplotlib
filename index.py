import pandas as pd
data = {
    'Teams' :[ 'Manchester united', 'Arsenal', 'Chelsea', 'Liverpool', 'Aston villa', 'Brenford', 'wolves' ],
    'Points' :[89, 78, 76, 74, 69, 55, 45],
    'Arena' :['Old Trafford', 'Emirates', 'Stanford Bridge','Anfield','Villa park', 'Gtech', 'Molineux']}

df = pd.DataFrame(data)

df.to_csv('my_data.csv', index=False)
df = pd.read_csv('my_data.csv')
print(df)
#Displaying the first row of the data set

print(df.head())

#checking the structure of data
print(df.info())

#missing value
print(df.isnull().sum())


# Step 5: Compute basic statistics
print("Basic Statistics of Numerical Columns:")
print(df.describe())

# Step 6: Perform groupings and compute mean
# Replace 'CategoryColumn' and 'NumericalColumn' with your column names
# Example: Grouping by 'Region' and calculating mean 'Sales'
grouped_data = df.groupby('CategoryColumn')['NumericalColumn'].mean()

print("\nMean of NumericalColumn for each CategoryColumn:")
print(grouped_data)

# Identify patterns or findings
print("\nFindings:")
top_category = grouped_data.idxmax()
top_mean_value = grouped_data.max()
print(f"The highest mean value for 'NumericalColumn' is in the category: {top_category}, with a value of {top_mean_value}.")











