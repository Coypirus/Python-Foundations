# Binary search
# Sort the list
# Upper, lower, and mid bounds

pos = -1

def search(list, n):

    l = 0 # Lower Bound
    u = len(list)-1 # Upper Bound

    while l <= u :
        mid = (l+u) // 2 #Integer Division

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n: #If n is greater than mid value, move up lower bound
                l = mid+1 #mid + 1 because we don't have to check for mid if we already know it is not n.
                #Also helps us break out of the loop
            else:
                u = mid-1 #If n is less than mid value, move down upper bound
        return False

list = [4,7,8,12,45,99]
n = 45

if search(list, n):
    print("Found at", pos)
else:
    print("Not Found")