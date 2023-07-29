#Q10. Write a program to define a simple class.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")
# Create an instance of the Person class

name=input("Enter the name")
age=int(input("Eter the age"))
person1 = Person(name,age)

# Call the introduce method
person1.introduce()

