#Q27. Write a program to validate integer input using exception handling.
def validate_integer_input():
    while True:
        try:
            number = int(input("Enter an integer: "))
            return number
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Example usage
integer = validate_integer_input()
print("Valid integer:", integer)
