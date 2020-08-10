class A:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class B:
    def feature3(self):
        print("Feature 4 working")

    def feature4(self):
        print("Feature 4 working")

#Multiple inheritance
class C(A,B):
    def feature5(self):
        print("Feature 5 working")

a1 = A()
b1 = B()
c1 = C()

