'''Q8. Write a python program to calculate the average of a given number using the lambda
function'''
# Get user input for a list of numbers
numbers = input("Enter a list of numbers, separated by spaces: ").split()
numbers = [int(num) for num in numbers]

# Calculate the average using lambda function
average = lambda num_list: sum(num_list) / len(num_list)

# Call the lambda function to calculate the average
result = average(numbers)

# Print the average
print(f"The average is: {result}")

