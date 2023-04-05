import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('path/to/data.csv')

# Perform EDA
print(data.head())
print(data.describe())

# Visualize the data
plt.hist(data['column'], bins=10)
plt.xlabel('Column')
plt.ylabel('Count')
plt.show()
