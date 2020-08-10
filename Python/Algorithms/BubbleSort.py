# Bubble Sort
# Easiest sorting technique

# Bubble sort works by using multiple iterations where in each iteration
# The largest value is brought to the right, then the next iteration
# Happens with all the remaining values, etc.


def sort(nums):
    for i in range(len(nums) - 1, 0, -1): #Go from last element to index position 1
        # After every iteration of i one value will be fixed.
        for j in range(i):  # Go up until the last unsorted element.
            if nums[j] > nums[j+1]: #If first value is greater than second value, swap.
                temp = nums[j]
                nums[j] = nums[j+1] # Use j+1 because range is until but not including,
                                    # and we still want to check the last value
                nums[j+1] = temp

nums = [5, 3, 8, 6, 7, 2]


sort(nums)
print(nums)