'''Table of Contents
Create a 2D Numpy Array
Accessing different elements of a Numpy Array
Basic Operations
'''
import numpy as np 
import matplotlib.pyplot as plt

# Create a list
list1 = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]

# Convert list to Numpy Array
# Every element is the same type
array1 = np.array(list1)
print(array1)

# Show the numpy array dimensions
print("dimensions: ", array1.ndim)

# Show the numpy array shape
print("shape: ", array1.shape)

# Show the numpy array size
print("size: ", array1.size)

# Access the element on the second row and third column
print("access the element on the second row and third column:", array1[1, 2])

# Access the element on the first row and first and second columns
print("access the element on the first row and first and second columns:", array1[0][0:2])

# Access the element on the first and second rows and third column
print("access the element on the first row and second rows and third column:", array1[0:2, 2])

'''
Basic Operations
'''
X = np.array([[1, 2], [3, 4]]) 
Y = np.array([[2, 1], [1, 2]]) 
# Add X and Y
Z = X + Y
# Multiply Y with 2
Z = 2 * Y
# Multiply X with Y
Z = X * Y
# Calculate the dot product
Z = np.dot(X,Y)
print(Z)
# Get the transposed of C
print(X)
print(X.T)