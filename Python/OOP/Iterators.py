# Iterators

nums = [7, 8, 9, 5]

# Behind the scenes of a for loop is an iterator.
it = iter(nums) # Convert the list into an iterator.

#An iterator gives you one value at a time.
print(it.__next__()) # Call __next__() to get the next value.
print(next(it)) # next() is another way to get the next value.

for i in it: # You can loop through an iterator as well.
    print(i)
print()

#Create your own iterator: You need iter() and next()
class TopTen:

    def __init__(self):
        self.num = 1

    def __iter__(self): # Marks the class as iterable. Required.
        return self  # Return the object of the iterator.

    def __next__(self): # Gives you the next number
        if self.num <= 10: #You need to specify an end condition
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration # Raise exception once end condition is met
        #StopIteration is handled internally.
        #Without the exception, __next__ would keep running and returning None


values = TopTen()


print(next(values)) # An iterator doesn't repeat values.
for i in values:
    # This will not make i=1 because the value was already passed to
    # The previous print statement above the loop.
    print(i)

