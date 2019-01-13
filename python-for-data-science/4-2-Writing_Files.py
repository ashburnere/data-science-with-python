'''Table of Contents
Writing files Text Files
'''

# print workspace
import os
print("current workspace", os.getcwd())

# We can open a file object using the method ** write()** to save the text file to a list. 
# To write the mode, argument must be set to write w*. Let’s write a file *Example2.txt with the line: “This is line A”
with open('example2.txt','w') as writefile:
    writefile.write("This is line A")

with open('example2.txt','w') as writefile:
    writefile.write("This is line A1\n")
    writefile.write("This is line B1\n")

# By setting the mode argument to append a you can append a new line as follows:
with open('example2.txt','a') as testwritefile:
    testwritefile.write("This is line C1\n")

# print the file
with open('example2.txt','r') as testwritefile:
    print(testwritefile.read())

'''
Copy a file
'''
# Let's copy the file Example2.txt to the file Example3.txt:
with open('example2.txt','r') as readfile:
    with open('example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)
