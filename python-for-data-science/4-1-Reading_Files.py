'''Table of Contents
Reading Text Files
'''

''' The text file "example1.txt" contains 3 lines
This is line 1 
This is line 2
This is line 3
'''

# print workspace
import os
print("current workspace", os.getcwd())

#  read the file:
example1="D:/WORKSPACES/data-science-with-python/resources/data/example1.txt"
file1 = open(example1,"r")

#The name of the file:
file1.name

# The mode the file object is in:
file1.mode

# We can read the file and assign it to a variable :
FileContent=file1.read()

# We can print the file:
print(FileContent)

#The file is of type string:
type(FileContent)

print("file closed? ", file1.closed)
# We must close the file object:
file1.close()


# Using the with statement is better practice, it automatically closes the file even if the code encounters an exception. 
# The code will run everything in the indent block then close the file object.
with open(example1,"r") as file1:
    FileContent=file1.read()
    print(FileContent)
print("file closed? ", file1.closed)

# only read the first 4 characters than the next 15
with open(example1,"r") as file1:
    print(file1.read(4))
    print(file1.read(15))

# read one line
with open(example1,"r") as file1:
    print("first line: " + file1.readline())

# We can use a loop to iterate through each line:
with open(example1,"r") as file1:
        i=0;
        for line in file1:
            print("Iteration" ,str(i),":",line)
            i=i+1;

#We can use the method readline() to save the text file to a list:
with open(example1,"r") as file1:
    FileasList=file1.readlines()
    print(FileasList[0])
