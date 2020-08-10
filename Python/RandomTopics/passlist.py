def count(lst):
    even, odd = 0

    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

lst = []

while True:
    print("Press q to quit.")
    x = input("Please enter integers to add to the list: ")
    if x.lower() == "q":
        break
    else:
        lst.append(int(x))


even, odd = count(lst)
print(f"Even: {even} and Odd: {odd}")