lst1 = [1, 2, 3, 4, 5]

lst2 = list(map(lambda n: n ** 3, lst1))
print(lst2)
lst3 = list(map(lambda n: n + 1, lst1))
print(lst3)
lst4 = list(map(lambda n: n - 1, lst1))
print(lst4)
lst5 = list(map(lambda n: n * 2, lst1))
print(lst5)
