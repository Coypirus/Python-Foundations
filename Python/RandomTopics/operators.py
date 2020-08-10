#Arithmetic operators
#Assignment operators
#Relational operators
#Logical operators
#Unary operators

#Arithmetic
x = 2
y = 3
print(x/y)

#Assignment
x += 2
print(x)
x *= 3
print(x)
a, b = 5, 6
print(a, b)

#Unary operators (Only have one operand.)
n = 7
n = -n #Negative sign is a unary operator operating on only one operand (n).
print(n, "\n")

#Relational
print(a < b)
print(a == b)
print(a > b)
a = 6
print(a <= b)
print(a >= b)
print(a != b, "\n")


#Logical
a = 5
b = 4
print(a < 8 and b < 5) #and - both must be true
print(a < 8 and b < 2)

print(a < 8 or b < 2) #or - at least one condition is true

x = True
print(not x) #Not - reverse operator
print(a<8 and not b<2)