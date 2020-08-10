# Ways to pass arguments:
# Position, keyword, default, variable length.

def person(name, age=18):
    print(name)
    print(age)

# Variable length arguments(*)
# *b becomes a tuple.
def sum(*b):
    c = 0
    for i in b:
        c = c + i
    print(c)

#Keyworded variable length arguments(**)
# **data becomes a dictionary of key:value pairs.
def persona(name, **data):

    print(name)
    for i,j in data.items():
        print(i, j)

# Position
person("navin", 28)
# Keyword
person(age=28, name="navin")
# Default
person("navin")
person("navin", 28)  # Overrides default
# Variable length
sum(5, 6, 34, 78)
# Keyworded variable length arguments
persona('navin', age=28, city='Mumbai', mob=9765432)