#Q28. Write a program to demonstrate use of IndexError
def demonstrate_index_error():
    my_list = [1, 2, 3, 4, 5]

    try:
        # Trying to access an element at an index that is out of range
        print(my_list[10])
    except IndexError:
        print("IndexError occurred: Index is out of range.")

# Example usage
demonstrate_index_error()
