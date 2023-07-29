#Q5. Write a program to find multiples of the given number
def find_multiples(number, count):
    multiples = []
    for i in range(1, count + 1):
        multiples.append(number * i)
    return multiples

# Get user input
num = int(input("Enter a number: "))
count = int(input("Enter the count of multiples: "))

# Find the multiples of the given number
multiples_list = find_multiples(num, count)

# Print the multiples
print(f"The multiples of {num} are: {multiples_list}")
