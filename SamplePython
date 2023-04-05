import pandas as pd

# Read a CSV file
data = pd.read_csv('mydata.csv')

# Read from a SQL database
import sqlite3
conn = sqlite3.connect('mydatabase.db')
data = pd.read_sql('SELECT * FROM mytable', conn)

# Drop missing values
data = data.dropna()

# Remove duplicates
data = data.drop_duplicates()

# Convert string to datetime
data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d')

# Group by category and get the mean value of each group
grouped_data = data.groupby('category')['value'].mean()

# Calculate the total value for each month
monthly_data = data.resample('M', on='date')['value'].sum()

import matplotlib.pyplot as plt

# Create a bar chart of category counts
category_counts = data['category'].value_counts()
plt.bar(category_counts.index, category_counts.values)
plt.show()

# Create a line chart of monthly values
monthly_data.plot()
plt.show()
