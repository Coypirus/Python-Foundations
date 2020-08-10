# Lambda in Python Part 2
# Where do we use these?
import functools

nums = [3,2,6,8,4,6,2,9]

#Fetch all even numbers.
#Use the filter function, which takes a function.
#It then uses that function to check which items to filter in/out.
evens = list(filter(lambda n : n % 2 == 0, nums))
print(evens)

#Map allows you to apply an operation to every item in a list.

doubles = list(map(lambda n : n * 2, evens))
print(doubles)

#Reduce allows you to get one value that you want from a list.
#Requires a function with 2 arguments

sum = functools.reduce(lambda a, b: a + b, doubles)
print(sum)