# Exceptions and errors

# Errors
    # Compile Time
        #Syntatical errors(Code can't compile)
    # Logical
        #Code gets compiled and gives wrong/unintended output
    # Runtime
        #Code gets compiled and has no logical error(works for normal operation)
        #Get error for specific input(you get error at runtime)

#Runtime error is hard because the mistake is done by the user.
#You have to take into account what mistakes a user might make/unexpected circumstances.
#Your software should not stop.

print("Hi!")

a = 5
b = 2 #If this is zero, print(a/b) will throw ZeroDivisionError

#You should always try to close a resource if you open it.
try: # The code that might have an exception.
    print("resource Open")
    print(a/b)
    k = int(input("Enter a number: "))
    print(k)

except ZeroDivisionError as e: # Except executes if there is an error.  It jumps out of the try block.
    print("Hey, you cannot divide a Number by Zero", e)

except ValueError as e:
    print("Invalid input!")

except Exception as e: # Put Exception at the end so it doesn't override other errors.
    print("Something went Wrong...")

finally: # Finally executes no matter what.
    print("resource Closed")

print("Bye!")