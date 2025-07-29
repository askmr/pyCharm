def addMul5(num):
    lst1 = []
    add = 0
    for i in range(1, num + 1):
        if i % 5 == 0:
            lst1.append(i)
    print(lst1)

    for i in lst1:
        add += i
    print(add)


num = int(input("Enter the number: \n"))
addMul5(num)
