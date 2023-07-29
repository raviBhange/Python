#Q21. Write a program to demonstrate use of delegates
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def calculate(operation, x, y):
    return operation(x, y)

# Define a lambda function as a delegate
delegate = lambda x, y: x / y

# Use the delegates to perform calculations
a=int(input("Enter The a Number :"))
b=int(input("Enter The b  Number  :"))
result1 = calculate(add, a, b)
result2 = calculate(subtract, a, b)
result3 = calculate(multiply, a, b)
result4 = calculate(delegate, a, b)

# Print the results
print(f"Addition: {result1}")
print(f"Subtraction: {result2}")
print(f"Multiplication: {result3}")
print(f"Delegate: {result4}")
