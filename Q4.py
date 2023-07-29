#Q4. Write a program to accept a number from the user and find the factorial of the number.

def factorial(number):
    if number == 0:
        return 1
    else:
        fact = 1
        for i in range(1, number + 1):
            fact *= i
        return fact

# Get user input
num = int(input("Enter a number: "))

# Calculate the factorial of the number
fact_result = factorial(num)

# Print the factorial result
print(f"The factorial of {num} is {fact_result}.")
