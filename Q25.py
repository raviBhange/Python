#Q25. Write a program to Validate email using regular expressions.
import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    match = re.match(pattern, email)
    if match:
        return True
    else:
        return False

# Example usage
email = input("Enter the Email :")
if validate_email(email):
    print("Email is valid.")
else:
    print("Email is not valid.")
