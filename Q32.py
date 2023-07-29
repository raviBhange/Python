#Q32. Write a python program to create a new file in another directory.
import os
arr=os.path.join("D:","Student.txt")
f=open(arr,'w+')
f.write("New File")
print("File is created")
f.close()	
