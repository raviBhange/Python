#Q6. Write a program to demonstrate the use of default parameters in methods.
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

# Calling the function with both parameters
greet("Ram", "Good morning")

# Calling the function with only the 'name' parameter
greet("Jay")
