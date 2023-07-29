#Q29. Write a program to demonstrate use of ZeroDivisionError.
def demonstrate_zero_division_error():
    try:
        dividend = int(input("Enter the dividend: "))
        divisor = int(input("Enter the divisor: "))
        result = dividend / divisor
        print("Result:", result)
    except ZeroDivisionError:
        print("ZeroDivisionError occurred: Cannot divide by zero.")
    except ValueError:
        print("ValueError occurred: Invalid input.")

# Example usage
demonstrate_zero_division_error()
