from numpy import *

arr1 = array([1, 2, 3, 4, 5])
arr2 = array([6, 1, 9, 3, 2])

# Vectorized operation: applying an operation to each element
arr1 = arr1 + 1  # Add 1 to each element
arr1 = arr1 - 1 # Subtract 1 from each element
arr3 = arr1 + arr2  # Add arrays' elements together

#Some array functions
print(arr3)
print(sin(arr1))
print(cos(arr1))
print(log(arr1))
print(sqrt(arr1))
print(sum(arr1))
print(min(arr1))
print(max(arr1))
sort(arr1)
print(arr1)
print(concatenate([arr1, arr2]))

# Aliasing - creating a new reference to the same object.
arr1 = array([2,6,8,1,3])
arr2 = arr1
print(arr1, id(arr1))
print(arr2, id(arr2))

# Shallow copy - Make another array that is dependent on the first array
# Changing 1 value will still change its counterpart.
arr2 = arr1.view()
arr1[1] = 7
print(arr1, id(arr1))
print(arr2, id(arr2))

# Deep Copy - the arrays aren't linked in any way
arr2 = arr1.copy()
arr1[1] = 8
print(arr1, id(arr1))
print(arr2, id(arr2))
