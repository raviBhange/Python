'''
Q39. Write a program to create numpy arrays and use the functions as reshape,flatten and
transpose? '''
import numpy as np

# Create a 1D array
arr1d = np.array([1, 2, 3, 4, 5,6])
print("1D array:")
print(arr1d)
print()

# Create a 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array:")
print(arr2d)
print()

# Reshape the 1D array into a 2D array
reshaped_arr = arr1d.reshape(2, 3)
print("Reshaped array:")
print(reshaped_arr)
print()

# Flatten the 2D array
flattened_arr = arr2d.flatten()
print("Flattened array:")
print(flattened_arr)
print()

# Transpose the 2D array
transposed_arr = arr2d.transpose()
print("Transposed array:")
print(transposed_arr)
