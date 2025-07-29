lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst1 = list(map(lambda x: x if x % 2 == 1 else x * x, lst))
print(lst1)

# lst2=list(filter)
lst2 = list(map(lambda x: x + 1 if x <= 3 else x, lst))
print(lst2)

lst3 = list(map(lambda x: x * 2 if x % 2 == 1 else x, lst))
print(lst3)

lst4 = list(map(lambda x: x ** 2 if x % 2 != 0 else x**3 , lst))
print(lst4)