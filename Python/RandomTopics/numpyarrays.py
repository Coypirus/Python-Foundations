# Python's built in array module doesn't support multidimensional arrays.
# So we use numpy

from numpy import *

# numpy.array() doesn't need a TypeCode, but can mention type using dtype=.
arr = array([1, 2, 3, 4, 5, 6.])
# numpy can implicitly convert between types since all elements must be same type
print(arr)
print(arr.dtype)

# linspace() requires start, stop, and # of parts you want
arr = linspace(0, 15, 16)  # Breaking the range into 16 parts(inc. start and stop as 2 parts at the ends)
# Returns floats.
print(arr)

# arange() requires start, stop, step
arr = arange(1, 15, 2) # Doesn't include the stop point.
print(arr)

# logspace() returns numbers evenly spaced on a log scale.
# Takes start, stop, and # of parts
arr = logspace(1, 40, 5)
print('%.2f' %arr[4])

# zeros() creates an array of zeroes. Default dtype is float.
arr = zeros(5)
print(arr)

# ones() creates an array of ones. Default dtype is float.
arr = ones(5, dtype=int)
print(arr)