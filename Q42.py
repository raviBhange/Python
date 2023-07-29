'''Q42. Write a python program to create the pandas series using a dictionary and specify the
index.'''
import pandas as pd

# Create a dictionary
data = {'A': 10, 'B': 20, 'C': 30, 'D': 40, 'E': 50}

# Specify the index
index = ['B', 'C', 'A', 'D', 'E']

# Create a Pandas Series from the dictionary with specified index
series = pd.Series(data, index=index)

# Print the Pandas Series
print(series)
