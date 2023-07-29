'''Q19. Write a program to calc discount based on SP using class and object, take product name,
rate and quantity as input.
the discount will be calculated as
if (order<10000):
discount=20%
if (order<50000):
discount=10%
if (order>50000):
discount=5%
'''

class DiscountCalculator:
    def __init__(self, product_name, rate, quantity):
        self.product_name = product_name
        self.rate = rate
        self.quantity = quantity
    
    def calculate_discount(self):
        order = self.rate * self.quantity

        if order < 10000:
            discount = 0.2 * order
        elif order < 50000:
            discount = 0.1 * order
        else:
            discount = 0.05 * order

        return discount

# Get user input for product details
product_name = input("Enter product name: ")
rate = float(input("Enter product rate: "))
quantity = int(input("Enter product quantity: "))

# Create an instance of the DiscountCalculator class
calculator = DiscountCalculator(product_name, rate, quantity)

# Calculate the discount
discount = calculator.calculate_discount()

# Print the result
print(f"The discount for {calculator.product_name} is: {discount}")
