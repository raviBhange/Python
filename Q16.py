#Q16. Write a program to demonstrate the use of super function.

class Vehicle:
    def __init__(self, name):
        self.name = name
    
    def start(self):
        print(f"{self.name} is starting.")

class Car(Vehicle):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    
    def start(self):
        super().start()
        print(f"The {self.color} car is ready to go.")

# Create an instance of the Car class
name=input("Enter the  Vehicle name:")
color=input("Enter  the Car color :")
car = Car(name, color)

# Call the start method
car.start()
