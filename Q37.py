'''Q37. Write a program using numpy to display array in the format
type of array,
dimension of array,
shape of array,size of array,
type of element of array
arrange the array
'''
import numpy as np

def display_array_info(arr):
    # Type of array
    print("Type of array:", type(arr))
    
    # Dimension of array
    print("Dimension of array:", arr.ndim)
    
    # Shape of array
    print("Shape of array:", arr.shape)
    
    # Size of array
    print("Size of array:", arr.size)
    
    # Type of element in array
    print("Type of element in array:", arr.dtype)
    
    # Arrange the array
    print("Arranged array:")
    print(np.sort(arr))

# Example usage
user_array = input("Enter the elements of the array separated by spaces: ")
my_array = np.array(user_array.split(), dtype=int)

display_array_info(my_array)
