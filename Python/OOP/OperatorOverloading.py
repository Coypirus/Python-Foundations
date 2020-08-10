# Operator Overloading
# Operators correspond with magic methods.

#a = 5
#b = 6
#print(a + b)
#print(int.__add__(a, b))  # This is getting called when you say a + b

#a = '5'
#b = '6'
#print(a + b)
#print(str.__add__(a, b))


# Magic methods - __add__(), __sub__(), __mul__(), etc.
# Always surrounded by __
# Work behind the scene

class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    # Note: you probably don't need to name it self because Student is calling it.
    # Convention?
    def __add__(self, other):  # Overload the + operator because its not defined in your custom class yet.
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return f'{self.m1} {self.m2}'


s1 = Student(58, 69)
s2 = Student(60, 0)
s3 = s1 + s2  # The first operand goes into self, the next one goes into other

if s1 > s2:
    print("s1 wins")
else:
    (print("s2 wins"))

a = 9
print(a) # Behind the scenes, this calls a.__str__()

print(s1) # This also calls __str__()
print(s2.__str__()) # Same thing as above.