#Q24. Write a program to validate phone number using regular expressions.
import re

def validate_phone_number(phone_number):
    pattern = r'^(\+\d{1,3}\s?)?(\(\d{1,4}\)\s?)?[\d\- ]{7,}$'
    match = re.match(pattern, phone_number)
    if match:
        return True
    else:
        return False

# Example usage
phone_number = input("Enter phone Number: ")
if validate_phone_number(phone_number):
    print("Phone number is valid.")
else:
    print("Phone number is not valid.")
