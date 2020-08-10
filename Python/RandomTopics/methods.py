# 1) Instance methods
# 2) Class methods
# 3) Static methods

# Unlike variables, class and static
# methods are not the same.

# Two types of instance methods:
# Accessor methods - fetch value of instance variable
# Mutator methods - modify value of instance variable

class Student:
    school = "Telusko"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # Instance methods - use self parameter.
    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    # Accessor method
    def get_m1(self):
        return self.m1

    # Mutator method
    def set_m1(self, value):
        self.m1 = value

    # Class methods - work with class variables
    # Use cls parameter.
    # Use @classmethod decorator
        # so you don't have to pass cls an argument when calling.
    @classmethod
    def getSchool(cls):
        return cls.school

    # Static method - not concerned with class variables or instance variables
    # Keep parameters blank - no self or cls
    # Use @staticmethod decorator
    @staticmethod
    def info():
        print("This is Student class.. in methods module")

s1 = Student(34, 47, 32)
s2 = Student(89, 32, 12)

print(s2.avg())
print(Student.getSchool())
print(s1.getSchool())

Student.info()