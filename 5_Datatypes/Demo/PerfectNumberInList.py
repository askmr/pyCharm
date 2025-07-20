lst = [5, 6, 13, 17, 28, 114, 200, 496, 500]

for i in lst:  # perfect number
    fs = 0
    lst1 = []
    for j in range(1, i):
        if i % j == 0:
            fs = fs + j
            lst1.append(j)
            if fs == i:
                print(i, "is a perfect number")
                print(lst1)
