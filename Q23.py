#Q23. Write a program using regular expression to remove all whitespaces from a string.
import re

def remove_whitespaces(string):
    pattern = r'\s+'  # Regular expression pattern to match one or more whitespaces
    result = re.sub(pattern, '', string)
    return result

# Example usage
input_string =input("Enter String  :")
result = remove_whitespaces(input_string)
print(result)
