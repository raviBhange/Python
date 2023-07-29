#Q1. Write a program to find whether a number is Even or Odd and Prime

def is_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Get user input
num = int(input("Enter a number: "))

# Check if the number is even or odd
even_odd = is_even_odd(num)
print(f"The number {num} is {even_odd}.")

# Check if the number is prime or not
prime = is_prime(num)
if prime:
    print(f"The number {num} is prime.")
else:
    print(f"The number {num} is not prime.")
