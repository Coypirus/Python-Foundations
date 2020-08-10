#Find the factorial of a number
def fact(num):
    
    f = 1

    for i in range(1, num+1):
        f = f*i
    return f

x = 5

result = fact(x)
print(result)