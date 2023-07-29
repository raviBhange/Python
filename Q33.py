#Q33. Write a program to copy contents from one file to another file in python.
# Open the source file in read mode
f1 = open("newFile.txt", "r")

# Open the destination file in write mode
f2 = open("newFile2.txt", "w")

# Read from the source file and write to the destination file
f2.write(f1.read())
print("Content copied successfully!")

# Close both files
f1.close()
f2.close()
