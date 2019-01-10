'''
Table of Contents
Say "Hello" to the world in Python
What version of Python are we using?
Writing comments in Python
Errors in Python
Does Python know about your error before it runs your code?
Exercise: Your First Program
Types of objects in Python
Integers
Floats
Converting from one object type to a different object type
Boolean data type
Exercise: Types
Expressions and Variables
Expressions
Exercise: Expressions
Variables
Exercise: Expression and Variables in Python'''

# Check the Python Version
import sys
print(sys.version)

# Practice on writing comments
print('Hello, Python!') # This line prints a string
# print('Hi')

# Integer
print(type(11))

# Float
print(type(2.14))

# String
print(type("Hello, Python 101!"))

# Convert 2 to a float
float(2)

# Casting 1.1 to integer will result in loss of information
int(1.1)

# Convert a string into an integer
int('1')

# Convert a string into an integer with error
#int('1 or 2 people')

# Convert the string "1.2" into a float
float('1.2')

# Convert an integer to a string
str(1)

# Type of True
print(type(True))

# Type of False
print(type(False))

# System settings about float type
print(sys.float_info)

# Division operation expression
resultFloat=25 / 6
print(resultFloat)
# Integer division operation expression
resultInt=25 // 6
print(resultInt)
