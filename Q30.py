#Q30. Write a program to calculate the square and cube of a number using Multithreading.
import threading

def calculate_square(number):
    square = number ** 2
    print("Square of", number, "is", square)

def calculate_cube(number):
    cube = number ** 3
    print("Cube of", number, "is", cube)

def calculate_square_and_cube(number):
    square_thread = threading.Thread(target=calculate_square, args=(number,))
    cube_thread = threading.Thread(target=calculate_cube, args=(number,))
    
    square_thread.start()
    square_thread.join()
    cube_thread.start()  
    cube_thread.join()

# Example usage
number = int(input("Enter a number: "))
calculate_square_and_cube(number)
