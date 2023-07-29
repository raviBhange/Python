#Q40. Write a program to save and load the array in binary and text files.
import numpy as np

# Create a NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Save the array to a binary file
np.save("array_binary.npy", arr)

# Save the array to a text file
np.savetxt("array_text.txt", arr)

# Load the array from the binary file
loaded_arr_binary = np.load("array_binary.npy")
print("Loaded array from binary file:")
print(loaded_arr_binary)
print()

# Load the array from the text file
loaded_arr_text = np.loadtxt("array_text.txt")
print("Loaded array from text file:")
print(loaded_arr_text)
