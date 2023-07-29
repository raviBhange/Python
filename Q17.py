'''Q17. Write a program to calculate the arc length of an angle by assigning values to the
radius and angle data attributes of the class ArcLength
'''
import math

class ArcLength:
    def __init__(self, radius, angle):
        self.radius = radius
        self.angle = angle
    
    def calculate_arc_length(self):
        arc_length = (2 * math.pi * self.radius * self.angle) / 360
        return arc_length

# Create an instance of the ArcLength class
radius = float(input("Enter the radius: "))
angle = float(input("Enter the angle in degrees: "))
arc = ArcLength(radius, angle)

# Calculate the arc length
result = arc.calculate_arc_length()

# Print the result
print(f"The arc length is: {result}")
