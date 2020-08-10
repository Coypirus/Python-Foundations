#Fibonacci sequence
#Each number is the sum of the two numbers before it.
#Start with 0 and 1.

def fib(n):
    a = 0
    b = 1

    if n<=0:
        return
    elif n==1:
        print(a)
        return

    print(a)
    print(b)

    for i in range(2,n):
        c = a + b
        a = b
        b = c
        print(c)

fib(10)