#Q13. Write a program to demonstrate the use of destructors in a class.
class Person:
    def __init__(self, name):
        """
        Constructor method for the Person class.
        Initializes the name attribute.
        """
        self.name = name
    
    def __del__(self):
        """
        Destructor method for the Person class.
        Performs cleanup operations when the object is destroyed.
        """
        print(f"Deleting the Person object for {self.name}.")
    
    def introduce(self):
        """
        Method to introduce the person.
        Prints the name of the person.
        """
        print(f"My name is {self.name}.")

# Create an instance of the Person class
name = input("Enter the person's name: ")
person = Person(name)

# Call the introduce method
person.introduce()

# Explicitly delete the object
del person
