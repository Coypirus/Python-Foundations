# CPU has 3 parts:
# 1) Control Unit
# 2) Arithmetic/Logic Unit - Arithmetic Unit performs calculations.
# 3) Memory Unit - Variables, Saving Data, etc.

#Logic Unit makes your computer think.

import math

if True:
    print("I'm right")

if False:
    print("This won't execute")

x = int(input("Pass a number: "))
r = x % 2
if r == 0:
    print("Even")
    if x > 5:
        print("Great")
    else:
        print("Not so great")
elif r == 1:
    print("Odd")

print("Bye")

x = int(input("1, 2, 3, or 4? "))
if(x == 1):
    print("One")
elif(x == 2):
    print("Two")
elif(x == 3):
    print("Three")
elif(x == 4):
    print("Four")
else:
    print("Wrong input")