def addVal(lst):
    add = 0
    c = 0
    avg = 0
    nlst1 = []
    for i in lst:
        i = int(i)
        nlst1.append(i)
    print(nlst1)

    for i in nlst1:
        add += i
        c += 1
        avg = add / c
    return add, avg


lst2 = input("Enter the numbers: \n").split()
total, avg = addVal(lst2)

print("Sum is:", total)
print("Avg is:", avg)
