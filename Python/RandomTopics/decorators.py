# Decorators - add extra features to an existing function
# Doesn't modify the source code of the original function.

def div(a, b):
    print(a / b)

#Currying
#Returning a function from a function
def smart_div(func):
    def inner(a, b):  # Number of arguments should match your original function
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner

div = smart_div(div) #Ready to pass inner parameters
div(2,4)

