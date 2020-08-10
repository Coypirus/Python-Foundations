# Global variable - variable defined outside a function.
# Can access a global variable inside or outside a function.
# You cannot use a local variable outside of the scope
# where it is created.
a = 10
print(a, id(a))

#Refer to a global variable in a function
def glbvarinfunc():
    a = 9 #Create a local variable a.

    #Access a global variable in a function with a local variable
    #That has the same name.
    x = globals()['a']
    print(x, id(x))

    #Change the global variable
    globals()['a'] = 15

glbvarinfunc()
print(a)