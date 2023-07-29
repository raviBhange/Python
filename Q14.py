#Q14. Write a program to demonstrate dynamic attribute of a class.
class Car:
    def __init__(self, brand):
        self.brand = brand

# Create an instance of the Car class
brand=input("Enter Brand Name")
car = Car(brand)

# Add dynamic attributes to the car object
car.color = "Red"
car.price = 50000

# Access the dynamic attributes
print(car.brand)  # Output: Tesla
print(car.color)  # Output: Red
print(car.price)  # Output: 50000

'''in this  example, we have a Car class with an __init__ method
that initializes the brand attribute. The class definition does not
include any other attributes.'''
