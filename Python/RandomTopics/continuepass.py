
for i in range(1, 101):

    if i % 3 == 0 and i % 5 == 0:
        continue

    print(i)

print("Bye")

for i in range(1, 101):

    if(i % 2 != 0):
        pass #Pass the if block, ignore it.
    else:
        print(i)

print("Bye")