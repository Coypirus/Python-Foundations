# Generators

# Generators are an inbuilt way to give you iterators.
# Generators are special types of iterators made using yield.
# Generators allow you to fetch one value at a time instead of
# storing a giant list into memory.  They generate values on the fly.

# Define a function, not a class, for a generator.
# Use yield instead of return to give a generator object.
# Unlike return, you can write multiple yield statements.

def topten():
    n = 1
    # Yield can be called multiple times
    # This makes the generator able to generate(not store) multiple values.
    while n <= 10:
        sq = n * n
        yield sq
        n += 1


values = topten() # Printing values will just give a generator object

# Call a generator like an iterator (because it is one)
for i in values:
    print(i)
