#Q15. Write a program to call class methods using objects.
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def multiply(x, y):
        return x * y

# Create an instance of the MathUtils class
math_obj = MathUtils()

# Call the class methods using the object
a=int(input("Enter the   a number "))
b=int(input("Enter the   a number "))

sum_result = math_obj.add(a, b)
product_result = math_obj.multiply(a,b)

# Print the results
print(f"Sum: {sum_result}")
print(f"Product: {product_result}")
