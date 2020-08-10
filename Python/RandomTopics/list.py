nums = [25,25,12,36,95,14,45]
nums.append(99) #Adds a value to the end.
nums.insert(7,30) #Adds 1 instance by position
nums.remove(25) #Removes 1 instance by value
nums.pop(0) #Removes 1 instance by position
nums.pop() #Using pop without a value removes the last element added.
print(nums)

del nums[2:]

print(f"Deleted every value after/including position 2: {nums}")

nums.extend([29,11,14,36]) #Adds multiple values.
print(f"Extended:{nums}")

print(f"Minimum:{min(nums)}")
print(f"Maximum:{max(nums)}")
print(f"Sum:{sum(nums)}")
nums.sort()
print(f"Sorted:{nums}")