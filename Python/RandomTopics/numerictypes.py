#None - A type for variables that are not assigned any value (Analogous to null)

#Numeric - Int, Float, Complex, Bool
num = 2.5
print(type(num)) #Float
num = 5
print(type(num)) #Int
num = 6+9j
print(type(num), "\n") #Complex (Number)

#Converting variable types.
a = 5.6
b = int(a) #Truncates the decimal.  Returns 5
print(b)

k = float(b)
print(k)

b = 5
k = 6
c = complex(b,k)
print(c, "\n")

#Booleans - true and false.
boole = b < k
print(boole)
print(type(boole), "\n")

#True is 1 and false is 0
print(f"True: {int(True)}")
print(f"False: {int(False)}")

