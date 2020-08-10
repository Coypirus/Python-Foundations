#Variables have a name, value, and address
num = 5
#id(name) gives the address of a variable
print(id(num))

name = "navin"
print(id(name))

a = 10
b = a
#All three will give the same address.
print(id(a))
print(id(b))
print(id(10))

#In python, if two variables have the same data, they will point to the same object.
    #This makes python more memory efficient.
#The address of a variable is not based on the variable name but on the object itself.
#One object, multiple variables pointing to it.

#Garbage collection: if nothing is tagging/using data, it will be garbage collected later.

#In Python, you can't make a variable constant.
    #Show your intention to make a variable constant by using all-caps.
PI = 3.14
print(PI)
PI = 3.15
print(PI)

