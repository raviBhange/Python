'''
Q43.Write a program to access the elements of series in pandas from csv file, also access the
element from
different positions'''
import pandas as pd

# Step 1: Read the CSV file into a DataFrame
data = pd.read_csv('data.csv')

# Step 2: Access the elements of the Series
# Access the entire "name" column as a Series
name_series = data['name']

# Access the element at index 1
element_at_index_1 = name_series[1]

# Access the element at position 2
element_at_position_2 = name_series.iloc[2]

# Access the element at the last position
element_at_last_position = name_series.iloc[-1]

# Print the Series and accessed elements
print("Series:")
print(name_series)
print("\nElement at index 1:", element_at_index_1)
print("Element at position 2:", element_at_position_2)
print("Element at last position:", element_at_last_position)

