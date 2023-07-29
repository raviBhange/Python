#Q11. Write a program to illustrate the creation of multiple objects for a class.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Create multiple objects of the Person class
person1 = Person("Jay", 25)
person2 = Person("Aman", 30)
person3 = Person("Raj", 35)

# Call the introduce method for each object
person1.introduce()
person2.introduce()
person3.introduce()
