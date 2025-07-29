# Homework-use dictionary and user def

lst = input("Enter the elements: \n").split()
print(lst)

lst1 = list(map(int, lst))
print(lst1)

lst2 = list(filter(lambda x: x % 2 == 0, lst1))
lst3 = list(filter(lambda x: x % 2 != 0, lst1))
print(lst2, lst3)
