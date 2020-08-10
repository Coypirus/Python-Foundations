# We use inner classes to improve readability.
# We use them when one class is only used by another class.
class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        #Construct object from inner class
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = Student('Navin', 2)
s2 = Student('Jenny', 3)

s1.show()


# You can create an object of inner class inside the outer class
# or you can create an object of inner class outside the outer class
# provided you use the outer class name to call it.

# Put self.lap = self.Laptop() in a method in the outer class
# OR
# Put lap1 = Student.Laptop() ouside the outer class
