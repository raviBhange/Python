#Q31 .Write a program to print a table of two numbers using thread synchronization.

import threading

def print_table(number, limit, lock):
    for i in range(1, limit + 1):
        # Acquire the lock to ensure exclusive access to the console
        lock.acquire()
        print(number, "x", i, "=", number * i)
        # Release the lock to allow other threads to acquire it
        lock.release()

def print_table_with_synchronization(number1, number2, limit):
    lock = threading.Lock()
    
    thread1 = threading.Thread(target=print_table, args=(number1, limit, lock))
    thread2 = threading.Thread(target=print_table, args=(number2, limit, lock))
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()

# Example usage
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
limit = int(input("Enter the limit: "))

print_table_with_synchronization(number1, number2, limit)
