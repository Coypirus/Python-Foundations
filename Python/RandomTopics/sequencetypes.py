#Sequence types
#List, sets, tuples, string, range

lst = [25,36,45,12]
print(type(lst), "\n")

s = {36, 12, 45, 15, 25, 15} #Sets can't repeat items
print(s)
print(type(s), "\n")

t = (25,36,4,57,12)
print(type(t), "\n")

str = "navin"
print(type(str), "\n")

#In python, we don't have a char type, only a string type.
st = 'a'
print(type(st))

#In python but not other languages, we have range.
print(range(10))
print(list(range(10)))
print(list(range(2,11,2)))