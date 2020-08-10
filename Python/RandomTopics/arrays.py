# Arrays are like lists but all objects must be of the same type.
# The advantage: More memory efficient
# Compiler can preallocate space for a known width data type.

from array import *

# array(TypeCode, Contents)
# To specify a type, use a TypeCode
# Unsigned - doesn't include negative integers(use Capital TypeCodes)

vals = array('i', [5, 9, -8, 4, 2])

newArr = array(vals.typecode, [a*a for a in vals])

for e in newArr:
    print(e)

i = 0
while i < len(newArr):
    print(newArr[i])
    i+=1
    