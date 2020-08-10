import sys

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())  # Default 1000

i = 0


def greet():
    global i  # Allows you to use global variable in a function
    i += 1
    print("Hello", i)
    greet()


greet()
