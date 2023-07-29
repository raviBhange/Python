'''
Q38.Write a program to create numpy array and use the functions as 0's,1's,lines space,random
function
and sum of array'''
import numpy as np

# Create an array of zeros
def create_zeros_array(rows, cols):
    return np.zeros((rows, cols))

# Create an array of ones
def create_ones_array(rows, cols):
    return np.ones((rows, cols))

# Create an array with linearly spaced values
def create_linspace_array(start, end, num):
    return np.linspace(start, end, num=num)

# Create an array with random values
def create_random_array(rows, cols):
    return np.random.random((rows, cols))

# Sum of array
def get_array_sum(arr):
    return np.sum(arr)

# Example usage
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

zeros_array = create_zeros_array(rows, cols)
print("Zeros Array:")
print(zeros_array)

ones_array = create_ones_array(rows, cols)
print("\nOnes Array:")
print(ones_array)

start = float(input("\nEnter the start value for linspace: "))
end = float(input("Enter the end value for linspace: "))
num = int(input("Enter the number of elements for linspace: "))

linspace_array = create_linspace_array(start, end, num)
print("\nLinspace Array:")
print(linspace_array)

random_array = create_random_array(rows, cols)
print("\nRandom Array:")
print(random_array)

# Get sum of array
array_sum = get_array_sum(random_array)
print("\nSum of Array:", array_sum)
