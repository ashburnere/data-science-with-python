''' Table of Contents
Preparation
What is Numpy?
    Type
    Assign Value
    Slicing
    Assign Value with List
    Other Attributes
Numpy Array Operations
    Array Addition
    Array Multiplication
    Product of Two Numpy Arrays
    Dot Product
    Adding Constant to a Numpy Array
Mathematical Functions
Linspace
'''

import time 
import sys
import numpy as np 
import matplotlib.pyplot as plt

# If you recall, a Python list is a container that allows you to store and access data. We can create a Python List as follows:
list1=["0",1,"two","3",4]

array1 = np.array(list1)
print(array1.dtype)

# A numpy array is similar to a list, it's usually fixed in size and each element is of the same type. 
# We can cast a list to a numpy array
array1=np.array([0,1,2,3, 4])
print(array1.dtype)

array1=np.array([0,1,2,3, 4.1])
print(array1.dtype)

''' As with lists, we can access each element via a square bracket:'''

# Print each element
print("a[0]:", array1[0])
print("a[1]:", array1[1])
print("a[2]:", array1[2])
print("a[3]:", array1[3])
print("a[4]:", array1[4])

# Check the type of the array
print(type(array1))

# Check the type of the values stored in numpy array
print(array1.dtype)

# Assign the first element to 100
array1[0] = 100

# Slicing the numpy array
array2 = array1[1:4]
print(array2)

# Set the fourth element and fifth element to 300 and 400
array1[3:5] = 300, 400
array2 = array1[1:5]
print(array2)

'''Assign Value with List
Similarly, we can use a list to select a specific index. The list ' select ' contains several values:
'''
# Create the index list
select = [0, 2, 3]
array2=array1[select]
print(array2)

# Assign the specified elements to new value
array1[select] = 100000
array2=array1[select]
print(array2)

'''Other Attributes
Let's review some basic array attributes using the array a:'''

# Create a numpy array
a = np.array([0, 1, 2, 3, 4])
# Get the size of numpy array
a.size
# Get the number of dimensions of numpy array
a.ndim
# Get the shape/size of numpy array
a.shape
# Get the mean of numpy array
mean = a.mean()
# Get the standard deviation of numpy array
standard_deviation=a.std()
# Get the smallest and biggest value in the numpy array
min_a = a.min()
max_a = a.max()

'''Numpy Array Operations'''
u = np.array([1, 0])
v = np.array([0, 1])

# Numpy Array Addition
z = u + v
print(z)

# Array Multiplication
y = np.array([1, 2])
z = 2 * y
print(z)

# Product of Two Numpy Arrays
u = np.array([1, 2])
v = np.array([3, 2])
z = u * v
print(z)

# Dot Product
z = np.dot(u, v)
print(z)

# Adding Constant to a Numpy Array
z = u + 1
print(z)

'''Mathematical Functions'''
# The value of pie
np.pi
# Create the numpy array in radians
x = np.array([0, np.pi/2 , np.pi])
# Calculate the sin of each elements
y = np.sin(x)

''' Linspace'''
# A useful function for plotting mathematical functions is "linespace". 
# Linespace returns evenly spaced numbers over a specified interval.
# We specify the starting point of the sequence and the ending point of the sequence. 
# The parameter "num" indicates the Number of samples to generate, in this case 5:

# Makeup a numpy array within [-2, 2] and 5 elements
z = np.linspace(-2, 2, num=5)
print(z)
# Makeup a numpy array within [-2, 2] and 9 elements
z = np.linspace(-2, 2, num=9)
print(z)

# Makeup a numpy array within [0, 2π] and 100 elements 
x = np.linspace(0, 2*np.pi, num=100)
# Calculate the sine of x list
y = np.sin(x)
# Plot the result
plt.plot(x, y)
plt.show()