'''
Table of Contents
What are Strings?
Indexing
Negative Indexing
Slicing
Stride
Concatenate Strings
Escape Sequences
String Operations
'''
# Use quotation marks for defining string
"Michael Jackson"
# Use single quotation marks for defining string
'Michael Jackson'

# Digitals and spaces in string
'1 2 3 4 5 6 '
# Special characters in string
'@#2_#]&*^%$'

# Assign string to variable
name = "Michael Jackson"

print(name, "length:", len(name))

# Print the first element in the string --> M
print(name[0])

# Print the last element in the string --> n
print(name[len(name)-1])

# Print the element on index 6 in the string --> l
print(name[6])
# Print the element on the 13th index in the string --> o
print(name[13])

# Print the last element in the string by using negativ indexing --> n
print(name[-1]) 
# Print the first element in the string by using negativ indexing --> M
print(name[-len(name)]) 

# Take the slice on variable name with only index 0 to index 3 --> Mich
print(name[0:4])
# Take the slice on variable name with only index 8 to index 11 --> Jack
print(name[8:12])

# Stride: Get every second element. The elments on index 0, 2, 4 ...
print(name[::2])
# Stride: Get every second element in the range from index 0 to index 4 --> Mca
print(name[0:5:2]) 

# Concatenate two strings
statement = name + " is the best"
print(statement) 

# Print the string for 3 times
print(3*statement)

# New line escape sequence
print(" Michael Jackson \n is the best" )
# Tab escape sequence
print(" Michael Jackson \t is the best" )
# Include back slash in string
print(" Michael Jackson \\ is the best" )
# r will tell python that string will be display as raw string
print(r" Michael Jackson \ is the best" )

'''
String operations
'''
# Convert all the characters in string to upper case
A = "Thriller is the sixth studio album"
print("before upper:", A)
B = A.upper()
print("After upper:", B)

# Replace the old substring with the new target substring is the segment has been found in the string
A = "Michael Jackson is the best"
B = A.replace('Michael', 'Janet')

# Find the substring in the string. Only the index of the first elment of substring in string will be the output
name = "Michael Jackson" # --> 5
print(name.find('el'))

# If cannot find the substring in the string -> result is -1
print(name.find('Jasdfasdasdf'))