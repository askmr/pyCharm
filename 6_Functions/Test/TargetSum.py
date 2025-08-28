def targetSum(lst):
    x = lst[0]
    y = lst[1]
    for i in lst:
        for j in lst:
            if i + j == 5:
                x = lst.index(j)
                y = lst.index(i)
                print(x, y)
            break
    return x, y


lst1 = [2, 3, 4, 5]
a, b = targetSum(lst1)
# print(a, b)
