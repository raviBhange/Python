#Q12. Write a program to demonstrate the use of constructor in a class.

class Person:
    def __init__(self, name, age):
        """
        Constructor method for the Person class.
        Initializes the name and age attributes.
        """
        self.name = name
        self.age = age
    
    def introduce(self):
        """
        Method to introduce the person.
        Prints the name and age of the person.
        """
        print(f"My name is {self.name} and I am {self.age} years old.")

# Create an instance of the Person class
person = Person("Joy", 25)

# Call the introduce method
person.introduce()
