#Q41. Write a python program to create the pandas series from an array.
import pandas as pd
import numpy as np

# Create an array
arr = np.array([10, 20, 30, 40, 50])

# Create a Pandas Series from the array
series = pd.Series(arr)

# Print the Pandas Series
print(series)
