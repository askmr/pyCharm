# to change items in list


lst = ['1', '2', '3', '4', '5']
lst1 = []

for i in lst:
    lst1.append(int(i))
print(lst1, type(lst1))

# use map() to avoid line num 4 to 6, as below

lst2 = list(map(int, lst))
print(lst2)
