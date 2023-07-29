'''Q7. Write a python program to calculate the total number of upper case and lower case
characters'''
def count_upper_lower(string):
    upper_count = 0
    lower_count = 0

    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

# Get user input
input_string = input("Enter a string: ")

# Calculate the count of uppercase and lowercase characters
upper, lower = count_upper_lower(input_string)

# Print the results
print(f"Total uppercase characters: {upper}")
print(f"Total lowercase characters: {lower}")

