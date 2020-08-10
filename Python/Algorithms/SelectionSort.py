# Selection Sort(Better)
# Less processing power than bubble sort.

# Find min value.
# Put min value all the way to the left and in next iteration
# Find the next min value to put on the left, one past the old min value.
# Repeat

# In each iteration, you only need to swap once!

def sort(nums):

    for i in range(len(nums)-1): # Finding min values: low to high index
        # Range of i is len(nums)-1 because this ends after the second to last element.
        # When there is only one value left it is the max value by default.
        minpos = i # Position of the current min value.
        for j in range(i, len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j

        #Swap
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)

nums = [5, 3, 8, 6, 7, 2]


sort(nums)
print(nums)