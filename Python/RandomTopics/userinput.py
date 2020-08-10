# Get user input.and convert
x = int(input("Enter 1st number: "))
print(type(x))
y = int(input("Enter 2nd number: "))
z = x + y
print(z)

# Get the first character that the user enters.
# Python doesn't have an actual character type.
ch = input("Enter a char: ")[0]
print(ch)

# Use .eval to evaluate an expression passed by the user.
# Eg. user passes 2 + 6 - 1

result = eval(input("Enter an expression: "))
print(result)

