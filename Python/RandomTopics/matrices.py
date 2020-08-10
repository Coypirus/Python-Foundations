from numpy import *

arr1 = array([
    [1, 2, 3, 6, 2, 9],
    [4, 5, 6, 7, 5, 3]

])

print(arr1)
print(arr1.ndim) # Get number of dimensions
print(arr1.shape) # Get tuple: (# of rows, # of columns)

# Flatten - Create 1D array from 2D array
arr2 = arr1.flatten()
print(arr2)

# Reshape - Convert a 1D array into a multidimensional array.
arr3 = arr2.reshape(2,2,3) # Each parameter is the size of a dimension.
             # Paremeters must multiply to the size of the 1D array.
print(arr3)  # reshape(2,2,3) gets an array of 2 arrays of 2 arrays of 3 values
print()

# Matrix - Depreciated, don't need to use this. Just use regular arrays.
# All these methods can now be used with regular arrays.
arr1 = array([
    [1,2,3,6],
    [4,5,6,7]
              ])

m = matrix(arr1)
print(m)
print()
m = matrix('1 2 3; 6 4 5; 1 6 7')
print(m)
print(diagonal(m))
print(multiply(m,m))

