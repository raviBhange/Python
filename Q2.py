#Q2. Write a program to find whether a number is Armstrong or not.
def is_armstrong(number):
    # Convert the number to a string to count the number of digits
    num_str = str(number)
    num_digits = len(num_str)

    # Calculate the sum of the cubes of each digit
    armstrong_sum = 0
    for digit in num_str:
        armstrong_sum += int(digit) ** num_digits

    # Check if the number is Armstrong or not
    if armstrong_sum == number:
        return True
    else:
        return False

# Get user input
num = int(input("Enter a number: "))

# Check if the number is Armstrong or not
if is_armstrong(num):
    print(f"The number {num} is an Armstrong number.")
else:
    print(f"The number {num} is not an Armstrong number.")
