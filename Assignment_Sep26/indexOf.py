def positionOf(lst, n):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == n:
                return (i, j)
    return None


lst1 = [2, 3, 4, 5]
target1 = 5
lst2 = [2, 3, 4]
target2 = 6
lst3 = [1, 5, 5, 4]
target3 = 10

print(positionOf(lst1, target1))
print(positionOf(lst2, target2))
print(positionOf(lst3, target3))
