# Pass arguments while starting the program
# Eg. python passarguments.py 5 2
# File name is index number 0.
# Arguments afterwards are indexed
import sys

# sys.argv accesses the arguments passed when starting the program
# However, all arguments are in string format.
x = int(sys.argv[1])
y = int(sys.argv[2])
z = x + y
print(z)