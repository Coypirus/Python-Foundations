#Sets are like lists, but they do NOT:
#1) Follow a sequence
#2) Support duplicate values


s = {22, 25, 14, 21, 5} #Does not follow a sequence!
print(s)
s = {25,14,98,64,75,98} #Values cannot repeat!
print(s)

#Uses a concept called hash to improve performance
#Does not use sequences in order to go as fast as possible
    #Therefore it also does not support indexing.

s.pop()
print(s)