#def fact(num):
#   if num == 0:
#       return 1
#   else:
#       return num*fact(num-1)

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

result = fact(5)
print(result)
