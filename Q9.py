'''Q9. Write a program to define multiple decorator functions to find out square root in the second
decorator and then factorial of square root in the first decorator function of a given number'''
import math

def square_root_decorator(func):
    def wrapper(number):
        result = func(number)
        sqrt_result = math.sqrt(result)
        print(f"The square root of {result} is: {sqrt_result}")
        return sqrt_result
    return wrapper

def factorial_decorator(func):
    def wrapper(number):
        result = func(number)
        factorial_result = 1
        for i in range(2, int(result) + 1):
            factorial_result *= i
        print(f"The factorial of the square root ({result}) is: {factorial_result}")
        return factorial_result
    return wrapper

@factorial_decorator
@square_root_decorator
def calculate(number):
    return number

# Get user input
num = int(input("Enter a number: "))

# Call the decorated function
calculate(num)
