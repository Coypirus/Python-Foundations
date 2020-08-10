# Type of polymorphism
# Dynamic typing

x = 5 # Get an integer space in memory

x = "Navin" # Get a String space in memory

# x is just a name!  It has no specific type.
# type(x) gets the type of 5 and "Navin", not x.

class PyCharm:

    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:

    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")

class Laptop:

    def code(self, ide):
        ide.execute()

ide = PyCharm()
ide2 = MyEditor()

lap1 = Laptop()
lap1.code(ide)
# ide parameter is not fixed to pycharm.
# You can assign it anything as long as it has an execute() method.
lap1.code(ide2)
