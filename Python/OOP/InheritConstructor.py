# When you create an object of subclass, it will call the subclass constructor
# Unless the subclass doesn't have one: then it will call the superclass constructor.
# To call both, use super() to access the __init__ method of the superclass.
class A:

    def __init__(self):
        print("In A init")

    def feature1(self):
        print("Feature 1-A working")

    def feature2(self):
        print("Feature 2 working")


class B:

    def __init__(self):
        print("In B init")

    def feature1(self):
        print("Feature 1-B working")

    def feature4(self):
        print("Feature 4 working")


# Method resolution order
# Whenever you have multiple inheritance it goes left to right.
# Applies to constructors and to methods.
class C(A, B):
    def __init__(self):
        super().__init__()
        print("in C init")

    def feat(self):
        super().feature2()  # You can also use super() to call methods from superclass.


a1 = C()
a1.feat()
