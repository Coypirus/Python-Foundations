# Method overloading and overriding are both part of polymorphism

# Overloading - 2 methods in the same class with same name, different # of parameters
# This concept is NOT in python

# Overriding - 2 methods with the same name
# Can't happen in same class but can happen with inheritance.


#Overloading - not supported in Python
#Instead, you can use default values or variable length arguments
class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        s = 0
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a
        return s


s1 = Student(58, 69)
print(s1.sum(5))


# Overriding
class A:

    def show(self):
        print("in A show")


class B(A):

    def show(self):
        print("In B show") # Overrides show() in parent class.


a1 = B()
a1.show()
