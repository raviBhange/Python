#Q34. Write a python program to count no. of lines in files.
def count_lines_in_file(filename):
    line_count = 0

    with open(filename, 'r') as file:
        for line in file:
            line_count += 1

    return line_count

# Example usage
filename = "newFile.txt"  

lines = count_lines_in_file(filename)
print("Number of lines in the file:", lines)
