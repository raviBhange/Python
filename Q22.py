#Q22. Write a program using regular expressions to find all the digits in a string.
import re

def find_digits(string):
    pattern = r'\d+'  # Regular expression pattern to match one or more digits
    digits = re.findall(pattern, string)
    return digits

# Example usage
input_string = input("Enter String  :")
result = find_digits(input_string)
print(result)
